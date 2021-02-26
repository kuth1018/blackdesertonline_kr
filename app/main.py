
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('BlackDesert Kr patch')
        self.move(300, 300)
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
        bdo_folder_label = QLabel('Black Desert Online installation folder', self)
        bdo_folder_label.move(20, 20)
        bdo_folder_path = QLabel('No data', self)
        bdo_folder_path.move(20, 40)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())