from pathlib import Path
import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import deepdream

class GUIWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.input_image = None

        self.layout = QVBoxLayout()

        self.select_input_image_button = QPushButton('Select input image')
        self.select_input_image_button.clicked.connect(self.select_input_image)
        self.layout.addWidget(self.select_input_image_button)

        self.dream_button  = QPushButton('Dream!')
        self.dream_button.clicked.connect(self.dream)
        self.layout.addWidget(self.dream_button)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('NeuralEasel')

    def select_input_image(self):
        file_dialog = QFileDialog()
        filepath = file_dialog.getOpenFileName(
                self,
                'Select input image',
                str(Path.home()),
                'Image files (*.jpg *.jpeg *.png)')[0]
        if filepath and len(filepath) > 0:
            self.input_image = filepath

    def dream(self):
        if self.input_image == None:
            mb = QMessageBox()
            mb.setWindowTitle('Select input image')
            mb.setText('Please set input image')
            mb.setIcon(QMessageBox.Warning)
            mb.exec_()
            return
        path = Path.home() / 'NeuralEasel'
        os.makedirs(path, exist_ok=True)
        deepdream.gui_run(self.input_image, path)

class GUIApplication:
    def __init__(self):
        self.app = QApplication([])
        self.main_window = GUIWindow()
        self.main_window.show()
        self.app.exec_()

def main():
    app = GUIApplication()

main()
