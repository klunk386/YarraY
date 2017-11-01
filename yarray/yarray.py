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

        base = super(MainWindow, self)
        base.__init__(None,
                      size=(800,600),
                      title="Yarray (Ver. {0})".format(YARRAY_VERSION),
                      *args, **kwargs)

        self.CreateMenu()
        self.CreateToolbar()

        #-----------------------------------------------------------------------

        splitter = wx.SplitterWindow(self, wx.ID_ANY)

        panel_1 = wx.Panel(splitter, wx.ID_ANY)
        panel_2 = wx.Panel(splitter, wx.ID_ANY)

        splitter.SplitVertically(panel_1, panel_2)
        splitter.SetSashGravity(0.25)

        box_1 = wx.BoxSizer(wx.VERTICAL)
        box_2 = wx.BoxSizer(wx.VERTICAL)
        panel_1.SetSizer(box_1)
        panel_2.SetSizer(box_2)

        prj_tree = ProjectTree(panel_1)
        box_1.Add(prj_tree, wx.ID_ANY, wx.EXPAND)

        hdr_list = HeaderList(panel_2)
        box_2.Add(hdr_list, wx.ID_ANY, wx.EXPAND)

        #-----------------------------------------------------------------------

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

    def OnQuit(self, event):

        self.Close()

# ==============================================================================

class ProjectTree(wx.TreeCtrl):

    def __init__(self, parent):

        base = super(ProjectTree, self)
        base.__init__(parent,
                      wx.ID_ANY,
                      wx.DefaultPosition,
                      wx.DefaultSize,
                      wx.TR_HAS_BUTTONS)

        root = self.AddRoot('Project')

# ==============================================================================

class HeaderList(wx.ListCtrl):

    def __init__(self, parent):

        base = super(HeaderList, self)
        base.__init__(parent,
                      wx.ID_ANY,
                      wx.DefaultPosition,
                      wx.DefaultSize)

# ==============================================================================

if __name__ == '__main__':

    YarraY()

