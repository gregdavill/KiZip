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
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ZiKip", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE|wx.BORDER_DEFAULT )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class SettingsPanelBase
###########################################################################

class SettingsPanelBase ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


    def __del__( self ):
        pass


###########################################################################
## Class SettingsDialogPanel
###########################################################################

class SettingsDialogPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer21 = wx.BoxSizer( wx.VERTICAL )

        self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        bSizer21.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )

        bSizer22 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button13 = wx.Button( self, wx.ID_ANY, u"Generate Gerbers", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer22.Add( self.m_button13, 0, wx.ALL, 5 )

        self.m_button14 = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer22.Add( self.m_button14, 0, wx.ALL, 5 )


        bSizer21.Add( bSizer22, 0, wx.ALIGN_CENTER, 5 )


        self.SetSizer( bSizer21 )
        self.Layout()

        # Connect Events
        self.m_button13.Bind( wx.EVT_BUTTON, self.OnGenerateGerbers )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnGenerateGerbers( self, event ):
        event.Skip()


