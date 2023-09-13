from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, QObject
from PyQt6.QtGui import QPalette, QWheelEvent, QColor, QColorConstants, QResizeEvent, QPainter, QBrush

from .ChatPreview import ChatPreview
from ..Boxes.ScrollStack import ScrollStack
from ..Back_End.Account import *

from ..Back_End import ApplicationController


class ChatList(ScrollStack):
    def __init__(self, parent: QObject | None = None):
        ScrollStack.__init__(self, parent)

        self.build()

    def reset(self):
        pass

    def build(self):
        for acc in ApplicationController.Application.Chats():
            self.addWidget(ChatPreview(acc))

