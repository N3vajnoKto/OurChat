from PyQt6.QtWidgets import QWidget, QGridLayout
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QResizeEvent, QPainter, QBrush

from .ChatList.ChatList import ChatList

class HomeSpace(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.resize(200, 300)
        self.setMinimumSize(200, 200)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColorConstants.Green)
        self.setPalette(pal)

        self.centralWidget = None

        lay = QGridLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(lay)

        self.setCentrealWidget(ChatList())

    def setCentrealWidget(self, w: QWidget = None):
        if (self.centralWidget != None):
            self.layout().removeWidget(self.centralWidget)
        self.centralWidget = w
        self.layout().addWidget(w)
