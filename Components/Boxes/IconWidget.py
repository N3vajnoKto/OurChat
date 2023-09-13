from PyQt6.QtWidgets import QWidget, QSplitter
from PyQt6.QtCore import QObject, Qt, pyqtSignal, QEvent
from PyQt6.QtGui import QPalette, QColorConstants, QPainter, QPaintEvent, QIcon


class IconWidget(QWidget):
    def __init__(self, icon: QIcon, parent: QObject | None = None):
        QWidget.__init__(self, parent)
        self.icon = icon

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.SmoothPixmapTransform)

        self.icon.paint(painter, self.rect())

    def setIcon(self, icon: QIcon):
        self.icon = icon

