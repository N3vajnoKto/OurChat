from typing import Optional

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication
from PyQt6.QtCore import Qt, QObject, pyqtSignal, QEvent, QPointF, pyqtSlot
from PyQt6.QtGui import QPalette, QWheelEvent, QColor, QColorConstants, QResizeEvent, QPainter, QBrush, QMouseEvent, \
    QCursor

from .VerticalScrollArea import VerticalScrollArea

class HidingVSArea(VerticalScrollArea):
    def __init__(self, parent: QObject | None = None):
        VerticalScrollArea.__init__(self, parent)

        self.maxSz = 200

    @pyqtSlot
    def hide(self):
        self.setFixedSize(0, 0)

    @pyqtSlot
    def open(self):
        if self.widget is not None:
            self.setMaximumSize(100000, min(self.widget.height(), self.maxSz))
        else:
            self.setMaximumSize(0, 0)
