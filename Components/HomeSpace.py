from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QPaintEvent, QPainter, QBrush


class HomeSpace(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.resize(200, 300)
        self.setMinimumSize(200, 200)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColorConstants.Blue)
        self.setPalette(pal)
