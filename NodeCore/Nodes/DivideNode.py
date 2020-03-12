#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Fireclaw the Fox"
__license__ = """
Simplified BSD (BSD 2-Clause) License.
See License.txt or http://opensource.org/licenses/BSD-2-Clause for more info
"""

from NodeCore.Nodes.NodeBase import NodeBase
from NodeCore.Sockets.InSocket import InSocket

class Node(NodeBase):
    def __init__(self, parent):
        NodeBase.__init__(self, "DIVIDE", parent)
        self.addOut("Out")
        self.addIn("In 1", InSocket)
        self.addIn("In 2", InSocket)

    def logic(self):
        """Divides the values given in the into nodes if both are set"""
        if self.inputList[0].value is None or self.inputList[1].value is None:
            self.outputList[0].value = float("NaN")
            return
        if self.inputList[1].value != 0:
            self.outputList[0].value = self.inputList[0].value / self.inputList[1].value
        else:
            self.outputList[0].value = float("NaN")
