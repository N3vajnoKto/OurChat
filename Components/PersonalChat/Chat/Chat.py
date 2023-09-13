from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QColorConstants

from .EditorBox import EditorBox
from .MessageList import MessageList
from .MessageInfo import MessageInfo

class Chat(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.messageBox = MessageList(self)
        self.editorBox = EditorBox(self)

        lay = QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)

        lay.addWidget(self.messageBox)
        lay.addWidget(self.editorBox)

        self.setLayout(lay)

        self.editorBox.editor.textSended.connect(self.sendMyMessage)

    def sendMyMessage(self, text: str):
        info = MessageInfo(text, 0, True)
        self.messageBox.addWidget(info)
        pass

