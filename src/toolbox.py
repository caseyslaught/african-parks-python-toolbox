import arcpy
import os
import sys

# prevent writing .pyc files
sys.dont_write_bytecode = True


class Toolbox(object):
    def __init__(self):
        self.label = "Garamba Python Toolbox"
        self.alias = "Garamba Python Toolbox"
        self.tools = [FetchPositions]


FetchPositions = object
