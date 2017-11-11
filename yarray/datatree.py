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

    def add_child(self, id, type='group', data=None):

        child = Node(id)
        child.parent = self
        child.type = type
        if data is not None:
            child.data = data
        self.child.append(child)
        return child

    def get_child(self, id):

        for child in self.child:
            if child.id == id:
                return child

    def del_child(self, id=None):

        for i in reversed(range(len(self.child))):
            if (id is None) or (self.child[i].id == id):
                self.child[i].del_child(None)
                del self.child[i]

    def get_path(self):

        path = [self.id]
        parent = self.parent
        while 1:
            if parent is None:
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

# ==============================================================================

class Array(object):
    """
    """

    def __init__(self):

        self.head = {'ID': '',
                     'NAME': '',
                     'NSTA': 0}
        self.data = []

    def __del__(self):
        print "Array deleted"

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

    def __del__(self):
        print "Trace deleted"
