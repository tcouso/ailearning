import sys
import os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPixmap

window_name, base_class = uic.loadUiType("board.ui")


class MainWindow(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image_path = os.path.join('widgets', 'o_tic-tac-toe.png')
        self.setMouseTracking(True)
        self.label_2.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        position = event.pos()
        print(position)
        self.label_2.setPixmap(QPixmap(self.image_path))
        self.label_2.setScaledContents(True)

    def mouse_placement(self):
        pass



if __name__ == '__main__':
    app = QApplication([])
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
