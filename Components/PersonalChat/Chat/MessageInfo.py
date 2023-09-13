import copy

from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QColorConstants, QFont, QFontMetrics

from typing import Self
from ... import UiController

class MessageInfo:
    def __init__(self, text: str = "Empty Message", time: int = 0, mine: bool = False, checked: bool = False):
        self.mine: bool = mine
        self.time: int = time
        self.checked: bool = checked
        self.text = text

        self.topConnecter: MessageInfo = None
        self.bottomConnecter: MessageInfo = None

    def connectTop(self, lnk: Self):
        if lnk is None:
            return
        self.topConnecter = lnk
        lnk.bottomConnecter = self

    def connectBottom(self, lnk: Self):
        if lnk is None:
            return
        self.bottomConnecter = lnk
        lnk.topConnecter = self

    def isConnectedFromTop(self) -> bool:
        return self.topConnecter is not None

    def isConnectedFromBottom(self) -> bool:
        return self.bottomConnecter is not None

    def timeInStr(self):
        return "15:15"

    def suits(self, other: Self) -> bool:
        res: bool = False
        if other.mine == self.mine:
            res = True

        return res

    def __copy__(self):
        res = MessageInfo()
        res.time = self.time
        res.mine = self.mine
        res.checked = self.checked
        res.text = self.text
        return res

class MessageInfoBox(QWidget):
    def __init__(self, info: MessageInfo, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.info = copy.copy(info)

        self.time = QLabel(info.timeInStr(), self)
        self.time.setFont(QFont(UiController.DefaultFontFamily, 10))

        m = QFontMetrics(self.time.font())

        w = int(m.boundingRect(self.time.text()).width())
        h = int(m.boundingRect(self.time.text()).height())

        self.time.resize(w + 6, h)

        pal = self.palette()
        pal.setColor(self.foregroundRole(), QColorConstants.Gray)
        self.setPalette(pal)

        self.resize(self.time.size())