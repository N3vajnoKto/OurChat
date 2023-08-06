from PyQt6.QtWidgets import QWidget, QPlainTextEdit
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QColorConstants


class MessageBox(QWidget):
    def __init__(self, parent: QObject = None):
        QWidget.__init__(self, parent)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.Gray)
        self.setPalette(pal)