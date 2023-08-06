from PyQt6.QtWidgets import QWidget, QHBoxLayout
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QColorConstants

from .Editor import Editor


class EditorBox(QWidget):
    def __init__(self, parent: QObject = None):
        QWidget.__init__(self, parent)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.White)
        self.setPalette(pal)

        self.editor = Editor(self)
        #
        lay = QHBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 5, 0, 5)
        lay.addWidget(self.editor)
        #
        self.setLayout(lay)
