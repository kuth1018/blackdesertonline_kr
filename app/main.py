import sys
import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QFileDialog, QAction


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.bdo_folder_path = ''
        self.initUI()

    def initUI(self):
        self.setWindowTitle('BlackDesert Kr patch')
        self.resize(400, 200)
        self.center()
        self.initWidgets()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initWidgets(self):
        label_bdo_folder = QLabel('Black Desert Online installation folder', self)
        label_bdo_folder.move(20, 20)
        label_bdo_folder_path = QLabel('No data', self)
        label_bdo_folder_path.move(20, 40)
        btn_folder_path = QPushButton('Path', self)
        btn_folder_path.move(250, 14)
        btn_patch = QPushButton('Change', self)
        btn_patch.move(15, 60)
        btn_patch.clicked.connect(self.changeEnFileToKrFile)

        programname = os.path.basename(__file__)
        programbase, ext = os.path.splitext(programname)
        settings = QtCore.QSettings("bdo_kr_patch", programbase)
        path = settings.value("folder_path")

        self.label_patch_result = QLabel('Result', self)
        self.label_patch_result.setScaledContents(True)
        self.label_patch_result.setWordWrap(True)
        self.label_patch_result.setFixedWidth(350)
        self.label_patch_result.setFixedHeight(60)
        self.label_patch_result.move(20, 90)
        if path is not None and len(path) != 0:
            self.label_patch_result.setText(path)
        btn_folder_path.clicked.connect(self.showDialog)


    def changeEnFileToKrFile(self):
        self.label_patch_result.setText('Update Button clicked')


    def showDialog(self):
        folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.bdo_folder_path = folderpath
        self.label_patch_result.setText(self.bdo_folder_path)
        programname = os.path.basename(__file__)
        programbase, ext = os.path.splitext(programname)  # extract basename and ext from filename
        settings = QtCore.QSettings("bdo_kr_patch", programbase)
        if len(self.bdo_folder_path) != 0:
            settings.setValue("folder_path", self.bdo_folder_path)


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())