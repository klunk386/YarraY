#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# ==============================================================================
#
# Copyright (C) 2017 Valerio Poggi
#
# This file is part of yarray.
#
# yarray is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# yarray is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with yarray.  If not, see <http://www.gnu.org/licenses/>.
#
# ==============================================================================

import wx

# ==============================================================================

YARRAY_VERSION = "0.0.1"

# ==============================================================================

class YarraY(object):
    """
    """

    def __init__(self, gui=True):

        self.data = []

        if gui:
            app = wx.App()
            MainWindow()
            app.MainLoop()

# ==============================================================================

class MainWindow(wx.Frame):

    def __init__(self, *args, **kwargs):

        Parent = super(MainWindow, self)
        Parent.__init__(None,
                        size=(800,600),
                        title="Yarray (Ver. {0})".format(YARRAY_VERSION),
                        *args, **kwargs)

        self.CreateMenu()
        self.CreateToolbar()
        self.CreateTree()

        self.Centre()
        self.Show(True)

    def CreateMenu(self):

        menubar = wx.MenuBar()
        menu_1 = wx.Menu()
        menu_2 = wx.Menu()
        menu_3 = wx.Menu()
        menu_4 = wx.Menu()
        menu_5 = wx.Menu()

        self.SetMenuBar(menubar)
        menubar.Append(menu_1, '&Project')
        menubar.Append(menu_2, '&Signals')
        menubar.Append(menu_3, '&Viewer')
        menubar.Append(menu_4, '&Tools')
        menubar.Append(menu_5, '&Help')

        menu_1_item_1 = menu_1.Append(wx.ID_EXIT,
                                      'Quit',
                                      'Quit application')
        self.Bind(wx.EVT_MENU, self.OnQuit, menu_1_item_1)

    def CreateToolbar(self):

        toolbar = self.CreateToolBar()

        icon_quit = wx.ArtProvider.GetBitmap(wx.ART_QUIT)
        tool_quit = toolbar.AddLabelTool(wx.ID_ANY, 'Quit', icon_quit)
        self.Bind(wx.EVT_TOOL, self.OnQuit, tool_quit)

        toolbar.Realize()

    def CreateTree(self):

        print 'to do'
        


    def OnQuit(self, event):

        self.Close()

# ==============================================================================

if __name__ == '__main__':

    YarraY()

