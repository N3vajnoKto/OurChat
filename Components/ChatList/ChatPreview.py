from typing import Optional

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel
from PyQt6.QtCore import Qt, QObject, QEvent
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QResizeEvent, QEnterEvent, QFont, QMouseEvent

from ..Boxes.Avatar import Avatar
from ..Boxes.TextLine import TextLine
from ..Boxes.ButtonBox import ButtonBox
from ..Back_End.Account import Account
from .. import UiController

class ChatPreview(ButtonBox):
    def __init__(self, acc: Optional[Account], parent: QObject | None = None):
        ButtonBox.__init__(self, parent)

        self.setFixedHeight(54)

        self.account = acc

        self.setAutoFillBackground(True)

        self.setMouseTracking(True)

        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.White)
        self.setPalette(pal)

        self.defColor: QColor = QColorConstants.White
        self.avatarBox = QWidget(self)
        self.infoBox = QWidget(self)
        self.info = TextLine(self.account.name(), self)
        self.subinfo = TextLine(self.account.name(), self)
        self.avatar = Avatar(acc, self.avatarBox)

        self.info.setFont(QFont(UiController.DefaultFontFamily, 10, QFont.Weight.Medium))
        self.info.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        lay = QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 7, 0, 7)
        lay.addWidget(self.info)
        lay.addWidget(self.subinfo)
        self.infoBox.setLayout(lay)

        self.avatarBox.setFixedSize(self.height() + 10, self.height())

        lay = QGridLayout(self.avatarBox)
        lay.setAlignment(self.avatar, Qt.AlignmentFlag.AlignCenter)
        lay.setContentsMargins(10, 5, 10, 5)
        lay.addWidget(self.avatar)
        self.avatarBox.setLayout(lay)

        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        lay.addWidget(self.avatarBox)
        lay.addWidget(self.infoBox)
        self.setLayout(lay)

    def setBColor(self, c: QColor):
        pal = self.palette()
        pal.setColor(self.backgroundRole(), c)
        self.setPalette(pal)

    def enterEvent(self, event: QEnterEvent) -> None:
        self.setBColor(QColorConstants.Gray)
        self.update()

    def leaveEvent(self, event: QEvent) -> None:
        self.setBColor(self.defColor)
        self.update()