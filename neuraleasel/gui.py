from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class GUIWindow(QMainWindow):
    def __init__(self):
        super().__init__()

class GUIApplication:
    def __init__(self):
        self.app = QApplication([])
        self.main_window = GUIWindow()
        self.main_window.show()
        self.app.exec_()

def main():
    app = GUIApplication()

