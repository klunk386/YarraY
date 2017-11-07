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

class Node(object):

    def __init__(self, id):

        self.id = id
        self.type = None
        self.parent = None
        self.child = []
        self.data = None

    def add_child(self, id, type='group', data=[]):

        child = Node(id)
        child.parent = self
        if type:
            child.type = type
        if data:
            child.data = data
        self.child.append(child)
        return child

    def get_child(self, id):

        for child in self.child:
            if child.id == id:
                return child

    def get_path(self):

        path = [self.id]
        parent = self.parent
        while 1:
            if not parent:
                break
            path.insert(0, parent.id)
            parent = parent.parent
        return path

class Database(Node):
    """
    The Database class implements a hierarchical data structure
    based on a tree of node objects (or groups).
    Arrays and traces are appended to the tree end-branches.
    """

    def __init__(self, project_name):

        Node.__init__(self, project_name)
        self.type = 'root'

    def add_node(self, name):

        if not isinstance(name, list):
            name = [name]
        node = self
        for id in name[:-1]:
            child = node.get_child(id)
            if not child:
                node = node.add_child(id)
        node.add_child(name[-1])

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


