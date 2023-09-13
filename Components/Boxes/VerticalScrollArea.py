from typing import Optional

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication
from PyQt6.QtCore import Qt, QObject, pyqtSignal, QEvent, QPointF
from PyQt6.QtGui import QPalette, QWheelEvent, QColor, QColorConstants, QResizeEvent, QPainter, QBrush, QMouseEvent, \
    QCursor

from .VWidget import VWidget


class VerticalScrollArea(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.widget: Optional[VWidget] = None

        self.min: int = -1
        self.max: int = -1

        self.inversed: bool = False

        self.setMouseTracking(True)

    def setWidget(self, w: QWidget):
        self.widget = w
        self.widget.setParent(self)
        self.format()

    def isInversed(self) -> bool:
        return self.inversed

    def setInversed(self, b: bool):
        self.inversed = b
        self.correct()

    def innerHeight(self) -> int:
        if self.widget is not None:
            return self.widget.height()
        else:
            return 0

    def format(self):
        if self.widget is None:
            return

        self.widget.resizeWidth(self.width())

        self.min = self.height() - self.widget.height()

        if self.isInversed():
            self.max = max(self.min, 0)
        else:
            self.max = 0

        self.correct()

    def correct(self):
        if self.widget is None:
            return


        if self.widget.y() > self.max:
            self.widget.move(0, self.max)

        if self.widget.y() < min(self.min, self.max):
            self.widget.move(0, min(self.min, self.max))

    def scrollTo(self, to: int):
        self.widget.move(0, to)
        self.min = self.height() - self.widget.height()

        if self.isInversed():
            self.max = max(self.min, 0)
        else:
            self.max = 0

        self.correct()

    def minimumScrollPoint(self):
        return self.min

    def maximumScrollPoint(self):
        return self.max


    def widget(self) -> QWidget:
        return self.widget

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.format()

    def wheelEvent(self, event: QWheelEvent) -> None:
        if self.widget is None:
            event.ignore()
            return

        h = event.angleDelta().y()
        h = min(h   , 40)
        h = max(h, -40)
        self.scrollTo(self.widget.y() + h)
        event.accept()

        ps = self.widget.mapFromGlobal(QCursor.pos())
        pos = QPointF(ps.x(), ps.y())
        me = QMouseEvent(QEvent.Type.MouseMove, pos,
                         Qt.MouseButton.NoButton, Qt.MouseButton.NoButton,
                         Qt.KeyboardModifier.NoModifier)

        QApplication.sendEvent(self, me)

