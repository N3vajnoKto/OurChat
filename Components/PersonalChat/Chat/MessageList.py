from typing import Optional

from PyQt6.QtWidgets import QWidget, QPlainTextEdit
from PyQt6.QtCore import QObject, Qt
from PyQt6.QtGui import QColorConstants, QResizeEvent

from .MessageBox import MessageBox
from .MessageBox import MessageInfo

from ... import UiController
from ...Boxes.VListWidget import VListWidget

class MessageList(VListWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        VListWidget.__init__(self, parent)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), UiController.ThemeColor)
        self.setPalette(pal)


        self.lastMessage: Optional[MessageBox] = None

        self.setContentsMargins(0, 7, 0, 7)



    def addMessage(self, info: MessageInfo):
        w = MessageBox(info, self)
        w.message.format()
        w.messageFrame.updateSize()
        w.arrange()

        if self.lastMessage is not None:
            prevInfo = self.lastMessage.message.info
            if info.suits(prevInfo):
                w.connectMessage(self.lastMessage)

        self.lastMessage = w
        self.addWidget(w)


