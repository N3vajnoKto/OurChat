from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QRect, QObject
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QResizeEvent, QPainter, QBrush, QIcon

from ... import UiController
from ...ChatList.ChatList import ChatList
from .SearchBox import SearchBox
from ...Boxes.IconButton import IconButton
from ...Boxes.VerticalScrollArea import VerticalScrollArea

class HomeSpace(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.resize(200, 300)
        self.setMinimumSize(200, 200)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColorConstants.Green)
        self.setPalette(pal)
        self.searchBox = SearchBox(self)
        self.chatList = ChatList(self)

        self.chatScroll = VerticalScrollArea(self)

        self.chatScroll.setWidget(self.chatList)

        self.chatScroll.setAutoFillBackground(True)
        pal = self.chatScroll.palette()
        pal.setColor(self.chatScroll.backgroundRole(), UiController.Light)
        self.chatScroll.setPalette(pal)


        lay = QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)

        lay.addWidget(self.searchBox)
        lay.addWidget(self.chatScroll)

        self.setLayout(lay)

        self.searchBox.searchLine.closeButton.clicked.connect(self.chatList.reset)
        self.searchBox.menuButton.clicked.connect(UiController.Chat.openSidebar)
