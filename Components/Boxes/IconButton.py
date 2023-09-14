from PyQt6.QtWidgets import QWidget, QSplitter
from PyQt6.QtCore import QObject, Qt, pyqtSignal, QEvent
from PyQt6.QtGui import QPalette, QColorConstants, QPainter, QPaintEvent, QIcon

from .ButtonBox import ButtonBox

class IconButton(ButtonBox):
    def __init__(self, icon: QIcon, parent: QObject | None = None):
        ButtonBox.__init__(self, parent)
        self.icon = icon


    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.SmoothPixmapTransform)

        self.icon.paint(painter, self.rect())
