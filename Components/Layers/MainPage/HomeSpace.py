from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QResizeEvent, QPainter, QBrush

from ...ChatList.ChatList import ChatList
from ...Boxes.SearchBox import SearchBox

class HomeSpace(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.resize(200, 300)
        self.setMinimumSize(200, 200)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColorConstants.Green)
        self.setPalette(pal)
        self.searchBox = SearchBox(self)
        self.centralWidget = None

        lay = QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.searchBox)
        self.setLayout(lay)

        self.chatList = ChatList()

        self.searchBox.searchLine.closeButton.clicked.connect(self.chatList.reset)

        self.setCentralWidget(self.chatList)

    def setCentralWidget(self, w: QWidget = None):
        if self.centralWidget is not None:
            self.layout().removeWidget(self.centralWidget)
        self.centralWidget = w
        self.layout().addWidget(w)
