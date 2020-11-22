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


###########################################################################
## Class LayerSettingsPanelBase
###########################################################################

class LayerSettingsPanelBase ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer25 = wx.BoxSizer( wx.VERTICAL )

        sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Layer Settings" ), wx.VERTICAL )

        SizerList = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow1 = wx.ScrolledWindow( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText8 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Layer Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        bSizer13.Add( self.m_staticText8, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Extension", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer13.Add( self.m_staticText9, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        bSizer12.Add( bSizer13, 0, wx.EXPAND, 5 )

        self.LayerPanelArea = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer12.Add( self.LayerPanelArea, 1, wx.ALL|wx.EXPAND, 5 )


        self.m_scrolledWindow1.SetSizer( bSizer12 )
        self.m_scrolledWindow1.Layout()
        bSizer12.Fit( self.m_scrolledWindow1 )
        SizerList.Add( self.m_scrolledWindow1, 1, wx.ALL|wx.EXPAND, 5 )


        sbSizer11.Add( SizerList, 1, wx.EXPAND, 5 )


        bSizer25.Add( sbSizer11, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer25 )
        self.Layout()

    def __del__( self ):
        pass


###########################################################################
## Class LayerItemPanelBase
###########################################################################

class LayerItemPanelBase ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        self.LayerEnabledCheckbox = wx.CheckBox( self, wx.ID_ANY, u"<Back SolderMask>", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.LayerEnabledCheckbox, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

        self.Extension = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.Extension, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


        self.SetSizer( bSizer11 )
        self.Layout()
        bSizer11.Fit( self )

    def __del__( self ):
        pass


###########################################################################
## Class AddLayerDialog
###########################################################################

class AddLayerDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Add Layer", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer28 = wx.BoxSizer( wx.VERTICAL )

        fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer3.AddGrowableCol( 1 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Layer", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )

        fgSizer3.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.LayerName = wx.StaticText( self, wx.ID_ANY, u"<Layer>", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.LayerName.Wrap( -1 )

        fgSizer3.Add( self.LayerName, 0, wx.ALL, 5 )

        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"var0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )

        fgSizer3.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.m_textCtrl4, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"var1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText14.Wrap( -1 )

        fgSizer3.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

        self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.m_textCtrl5, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer28.Add( fgSizer3, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer28.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        bSizer29 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button21 = wx.Button( self, wx.ID_OK, u"Confirm", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer29.Add( self.m_button21, 0, wx.ALL, 5 )

        self.m_button20 = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer29.Add( self.m_button20, 0, wx.ALL, 5 )


        bSizer28.Add( bSizer29, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer28 )
        self.Layout()
        bSizer28.Fit( self )

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


