from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QColorConstants

from .EditorBox import EditorBox
from .MessageList import MessageList
from .MessageInfo import MessageInfo

from ... import UiController
from ...Boxes.VerticalScrollArea import VerticalScrollArea

class ChatWidget(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.messageList = MessageList()
        self.editorBox = EditorBox(self)

        lay = QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 1, 0, 0)

        self.scrollArea = VerticalScrollArea(self)

        pal = self.scrollArea.palette()
        pal.setColor(self.scrollArea.backgroundRole(), UiController.ThemeColor)
        self.scrollArea.setPalette(pal)
        self.scrollArea.setInversed(True)

        self.scrollArea.setWidget(self.messageList)

        lay.addWidget(self.scrollArea)
        lay.addWidget(self.editorBox)

        self.setLayout(lay)

        self.editorBox.editor.textSended.connect(self.sendMyMessage)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), UiController.ThemeColor)
        self.setPalette(pal)

        for i in range(10):
            info = MessageInfo("just a message")
            self.messageList.addMessage(info)

        info = MessageInfo("Hello", 0, True)
        self.messageList.addMessage(info)

        info = MessageInfo("My name is Nickname", 0, True)
        self.messageList.addMessage(info)

        info = MessageInfo("realy long sentence, realy long sentence, realy long sentence, realy long sentence, realy long sentence, realy long sentence", 0, True)
        self.messageList.addMessage(info)

        info = MessageInfo("goodbye", 0, True)
        self.messageList.addMessage(info)

    def sendMyMessage(self, text: str):
        info = MessageInfo(text, 0, True)
        self.messageList.addMessage(info)
        self.scrollArea.scrollTo(self.scrollArea.min)

