from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import QObject
from PyQt6.QtGui import QColorConstants

from .EditorBox import EditorBox
from .MessageList import MessageList

class Chat(QWidget):
    def __init__(self, parent: QObject = None):
        QWidget.__init__(self, parent)

        self.messageBox = MessageList(self)
        self.editorBox = EditorBox(self)

        lay = QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)

        lay.addWidget(self.messageBox)
        lay.addWidget(self.editorBox)

        self.setLayout(lay)
