# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class SettingsDialogBase
###########################################################################

class SettingsDialogBase ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ZiKip", pos = wx.DefaultPosition, size = wx.Size( 320,400 ), style = wx.DEFAULT_DIALOG_STYLE|wx.BORDER_DEFAULT )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class SettingsDialogPanel
###########################################################################

class SettingsDialogPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 320,380 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer21 = wx.BoxSizer( wx.VERTICAL )

        self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        bSizer21.Add( self.notebook, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button15 = wx.Button( self, wx.ID_ANY, u"Save Settings", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer22.Add( self.m_button15, 0, wx.ALIGN_LEFT|wx.ALL, 5 )


        bSizer22.Add( ( 50, 0), 1, wx.EXPAND, 5 )

        self.m_button13 = wx.Button( self, wx.ID_ANY, u"Generate Gerbers", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer22.Add( self.m_button13, 0, wx.ALL, 5 )

        self.m_button14 = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer22.Add( self.m_button14, 0, wx.ALL, 5 )


        bSizer21.Add( bSizer22, 0, wx.ALIGN_CENTER, 5 )


        self.SetSizer( bSizer21 )
        self.Layout()

        # Connect Events
        self.m_button15.Bind( wx.EVT_BUTTON, self.OnSaveSettings )
        self.m_button13.Bind( wx.EVT_BUTTON, self.OnGenerateGerbers )
        self.m_button14.Bind( wx.EVT_BUTTON, self.OnExit )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnSaveSettings( self, event ):
        event.Skip()

    def OnGenerateGerbers( self, event ):
        event.Skip()

    def OnExit( self, event ):
        event.Skip()


###########################################################################
## Class GeneralSettingsPanelBase
###########################################################################

class GeneralSettingsPanelBase ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 320,400 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer23 = wx.BoxSizer( wx.VERTICAL )

        sbSizer10 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Destination" ), wx.VERTICAL )

        fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer2.AddGrowableCol( 1 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText10 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        fgSizer2.Add( self.m_staticText10, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.outputDirPicker = wx.DirPickerCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_SMALL|wx.DIRP_USE_TEXTCTRL )
        fgSizer2.Add( self.outputDirPicker, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

        self.m_staticText11 = wx.StaticText( sbSizer10.GetStaticBox(), wx.ID_ANY, u"Name format", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        fgSizer2.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

        self.fileNameFormatTextControl = wx.TextCtrl( sbSizer10.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer24.Add( self.fileNameFormatTextControl, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_button16 = wx.Button( sbSizer10.GetStaticBox(), wx.ID_ANY, u"?", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        bSizer24.Add( self.m_button16, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 4 )


        fgSizer2.Add( bSizer24, 1, wx.EXPAND, 5 )


        sbSizer10.Add( fgSizer2, 1, wx.EXPAND, 5 )


        bSizer23.Add( sbSizer10, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer23.Add( ( 0, 0), 2, wx.EXPAND, 5 )


        self.SetSizer( bSizer23 )
        self.Layout()

        # Connect Events
        self.m_button16.Bind( wx.EVT_BUTTON, self.OnNameFormatHintClick )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnNameFormatHintClick( self, event ):
        event.Skip()


