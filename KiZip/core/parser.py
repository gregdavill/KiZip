import os
import tempfile
import sys

import pcbnew
import time

import logging


from pcbnew import *
from datetime import datetime
from shutil import copy

class Parser(object):

    def __init__(self, file_name, config, logger, board=None):
        self.file_name = file_name
        self.config = config
        self.logger = logger
        self.output_folder = None
        self.temp_folder = None
        self.generated_files = []

        self.board = board
        if self.board is None:
            self.board = pcbnew.LoadBoard(self.file_name)  # type: pcbnew.BOARD

    def __del__(self):
        if self.temp_folder is not None:
            self.temp_folder.cleanup()

    def parse(self):
        title_block = self.board.GetTitleBlock()
        file_date = title_block.GetDate()
        if not file_date:
            file_mtime = os.path.getmtime(self.file_name)
            file_date = datetime.fromtimestamp(file_mtime).strftime(
                    '%Y-%m-%d %H:%M:%S')
        title = title_block.GetTitle()
        pcb_file_name = os.path.basename(self.file_name)
        if not title:
            # remove .kicad_pcb extension
            title = os.path.splitext(pcb_file_name)[0]

        pcbdata = {
            "metadata": {
                "title": title,
                "revision": title_block.GetRevision(),
                "company": title_block.GetCompany(),
                "date": file_date,
            },
        }

        return pcbdata

    def plot(self):

        plot_plan = [
            ( "CuTop", F_Cu, "Top layer", ".gtl"),
            ( "CuBottom", B_Cu, "Bottom layer", ".gbl"),
            ( "MaskBottom", B_Mask, "Mask Bottom", ".gbs"),
            ( "MaskTop", F_Mask, "Mask top", ".gts"),
            ( "PasteBottom", B_Paste, "Paste Bottom", ".gbp"),
            ( "PasteTop", F_Paste, "Paste Top", ".gtp"),
            ( "SilkTop", F_SilkS, "Silk Top", ".gto"),
            ( "SilkBottom", B_SilkS, "Silk Bottom", ".gbo"),
            ( "EdgeCuts", Edge_Cuts, "Edges", ".gko"),
        ]

        self.temp_folder = tempfile.TemporaryDirectory(prefix="kizip")
        self.output_folder = self.temp_folder.name

        # Default
        pctl = PLOT_CONTROLLER(self.board)

        popt = pctl.GetPlotOptions()
        popt.SetOutputDirectory(self.output_folder)
        popt.SetPlotFrameRef(False)
        
        # Nightly doesn't like SetLineWidth
        try:
            popt.SetLineWidth(FromMM(0.35))
        except AttributeError:
            pass

        # Set some important plot options:
        popt.SetPlotFrameRef(False)
        popt.SetAutoScale(False)
        popt.SetScale(1)
        popt.SetMirror(False)
        popt.SetUseGerberAttributes(False)
        popt.SetExcludeEdgeLayer(True)
        popt.SetScale(1)
        popt.SetUseAuxOrigin(False)
        popt.SetNegative(False)
        popt.SetPlotReference(True)
        popt.SetPlotValue(True)
        popt.SetPlotInvisibleText(False)
        popt.SetSubtractMaskFromSilk(True) #remove solder mask from silk to be sure there is no silk on pads
        popt.SetMirror(False)
        popt.SetDrillMarksType(PCB_PLOT_PARAMS.NO_DRILL_SHAPE)

        # Create files and keep track of names
        for layer_info in plot_plan:
            pctl.SetLayer(layer_info[1])
            pctl.OpenPlotfile(layer_info[0], PLOT_FORMAT_GERBER, layer_info[2])
            pctl.PlotLayer()
            time.sleep(0.01)
            pctl.ClosePlot()
            # Create a copy with same filename and Protel extensions.
            srcPlot = pctl.GetPlotFileName()
            self.generated_files += [srcPlot]


        #generate internal copper layers, if any
        lyrcnt = self.board.GetCopperLayerCount();

        for innerlyr in range ( 1, lyrcnt-1 ):
            pctl.SetLayer(innerlyr)
            lyrname = 'inner%s' % innerlyr
            pctl.OpenPlotfile(lyrname, PLOT_FORMAT_GERBER, "inner")
            pctl.PlotLayer()
            time.sleep(0.01)
            pctl.ClosePlot()
            # Create a copy with same filename and Protel extensions.
            srcPlot = pctl.GetPlotFileName()
            self.generated_files += [srcPlot]

        # Fabricators need drill files.
        # sometimes a drill map file is asked (for verification purpose)
        drlwriter = EXCELLON_WRITER( self.board )
        drlwriter.SetMapFileFormat( PLOT_FORMAT_PDF )

        mirror = False
        minimalHeader = False

        if popt.GetUseAuxOrigin():
            def aux_origin_missing():
                popt.SetUseAuxOrigin(False)
                return wxPoint(0, 0)
            offset = getattr(self.board, "GetAuxOrigin", aux_origin_missing)()
        else:
            offset = wxPoint(0,0)
            
        mergeNPTH = False
        drlwriter.SetOptions( mirror, minimalHeader, offset, mergeNPTH )

        metricFmt = True
        drlwriter.SetFormat( metricFmt )

        genDrl = True
        genMap = True
        drlwriter.CreateDrillandMapFilesSet( self.output_folder, genDrl, genMap );

        project_name = os.path.splitext(os.path.split(self.file_name)[1])[0]

        drlPlot = os.path.join(self.output_folder,project_name + '-PTH.drl')
        self.generated_files += [drlPlot]
        
        drlPlot = os.path.join(self.output_folder,project_name + '-NPTH.drl')
        self.generated_files += [drlPlot]

        return self.generated_files
