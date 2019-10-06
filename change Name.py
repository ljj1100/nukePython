import sys

from PySide import QtUiTools
from PySide import QtGui
from PySide import QtCore


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.import_designQT()

    def import_designQT(self):
        loader = QtUiTools.QUiLoader()
        file = QFile("Z:/shows/z_fx_rnd/sharedFolder/pyqt_ui/design/nuke_design.ui")
        file.open(QFile.ReadOnly)

        self.myWidget = loader.load(file, self)
        self.editTxt = self.myWidget.findChildren(QLineEdit)
        self.pushButton = self.myWidget.findChildren(QPushButton)
        self.pushButton[0].clicked.connect(self.find_textEdit)

        self.myWidget.show()

    def find_textEdit(self):
        self.renameFilePath(nuke.selectedNodes(), self.editTxt[0].text())

    def renameFilePath(self, sel_node ,new_name):
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
                special_string = re.compile("(.+)(\W\d+)")
                split_fileName = special_string.search(name)
                change_name    = re.sub(split_fileName.group(1), new_name, name)
                new_setName    = "{}{}".format(change_name, ext)
                new_setPath    = "{}/{}".format(file_parentPath, new_setName)
                ##### set path #####
                os.rename(origin_path, new_setPath)

            reload_path = "{}/{}.####{}".format(file_parentPath, new_name, ext)
            node.knob("file").setValue(reload_path)

a = MainWindow()

