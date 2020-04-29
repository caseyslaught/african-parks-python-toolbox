import arcpy
import os
import sys

# prevent writing .pyc files
sys.dont_write_bytecode = True


class Toolbox(object):
    def __init__(self):
        self.label = "African Parks Python Toolbox"
        self.alias = "African Parks Python Toolbox"
        self.tools = [GetPositions]


# Tool names
GetPositions = object
