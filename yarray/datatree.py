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

class Project(object):
    """
    The project class implements a hierarchical data structure in JSON format.
    Arrays and traces are appended to the tree end-branches.
    Groups can be arbitrary nested within the tree.
    Example structure:
    data = {
    "name" : "Project Name",
    "type" : "project",
    "nodes" : [
              {
              "name": "Group 1",
              "type": "group",
              "nodes": [
                       {
                       "name": "Group 2",
                       "type": "group",
                       "nodes":[
                               Array()
                               Array()
                               Trace()
                               ]
                       },
                       Array()
                       Tarce()
                       ]
              },
              {
              "name": "Group 2",
              "type": "group",
              "nodes": []
              }
              ]
    }
    """

    def __init__(self, project_name):

        self.data = {'name': project_name,
                     'type': 'project',
                     'nodes': []}

    def GetPointer(self, path=[]):

        pointer = self.data
        for name in path:
            for node in pointer['nodes']:
                if node['name'] == name:
                    pointer = node
        return pointer

    def AddNode(self, group_name, path=[]):

        node = {'name': group_name,
                'type': 'group',
                'nodes': []}

        pointer = self.GetPointer(path)
        pointer['nodes'].append(node)

    def DelNode(self, group_name, path=[]):

        pointer = self.GetPointer(path)
        for node in pointer['nodes']:
            if node['name'] == group_name:
              pointer['nodes'].remove(node)

    def AddItem(self, item, path=[]):

        pointer = self.GetPointer(path)
        pointer['nodes'].append(item)

    def GetItemById(self, item_id, path=[]):

        pointer = self.GetPointer(path)
        for node in pointer['nodes']:
            if node['id'] == item_id:
                return node


# ==============================================================================

class Array(object):
    """
    """

    def __init__(self):

        self.head = {'ID': '',
                     'NAME': '',
                     'NSTA': 0}
        self.data = []

# ==============================================================================

class Trace(object):
    """
    """

    def __init__(self):

        self.head = {'ID': '',
                     'NAME': '',
                     'LEN': 0.,
                     'DT': 0.,
                     'T0': [0,0,0,0,0,0.],
                     'CRD': [0.,0.,0.],
                     'CHN': 0,
                     'CHL': [],
                     'ROT': [0.,0.,0.],
                     'UNITS': '',}
        self.data = []

