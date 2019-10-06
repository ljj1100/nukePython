

from PySide.QtGui import *
from PySide.QtCore import *

class CreateNukeUI(QWidget):
    def __init__(self):







selected_nodes = nuke.selectedNodes()

def renameFilePath(sel_node ,new_name):
    import os
    import re

    for node in sel_node:
        file_path       = node.knob("file").value()
        file_pathSplit  = file_path.split("/")

        ##### import listDir #####
        file_parentPath = "/".join(file_pathSplit[:-1])
        children_list   = os.listdir(file_parentPath)
        ##### sort list      #####
        children_list.sort()

        for file_name in children_list:
            origin_path    = "{}/{}".format(file_parentPath, file_name)
            name, ext      = os.path.splitext(file_name)
            special_string = re.compile("\W")
            split_fileName = re.split(special_string ,name)
            change_name    = re.sub(split_fileName[0], new_name, name)
            new_setName    = "{}{}".format(change_name, ext)
            new_setPath    = "{}/{}".format(file_parentPath, new_setName)
            ##### set path #####
            os.rename(origin_path, new_setPath)

        reload_path = "{}/{}.####{}".format(file_parentPath, new_name, ext)
        node.knob("file").setValue(reload_path)

renameFilePath(selected_nodes, "test")