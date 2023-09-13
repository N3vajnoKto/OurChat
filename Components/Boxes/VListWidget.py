from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication
from PyQt6.QtCore import Qt, QObject, pyqtSignal, QEvent, QPointF
from PyQt6.QtGui import QPalette, QWheelEvent, QColor, QColorConstants, QResizeEvent, QPainter, QBrush, QMouseEvent, \
    QCursor

from .VWidget import VWidget


class VListWidget(VWidget):
    def __init__(self, parent: QObject | None = None):
        VWidget.__init__(self, parent)
        self.widgetList: list[VWidget] = []
        self.defaultSpacing: int = 0
        self.spacing: list[int] = []

        self.resize(0, 0)

    def addWidget(self, widget: VWidget, pos: int = -1):
        widget.setParent(self)
        widget.resizeWidth(self.width() - self.contentsMargins().left() - self.contentsMargins().right())
        self.widgetList.append(widget)
        h = max(self.contentsMargins().top(), self.height() - self.contentsMargins().bottom())


        if len(self.spacing) != 0:
            h += self.spacing[-1]
        widget.move(self.contentsMargins().left(), h)
        h += widget.height()
        self.spacing.append(self.defaultSpacing)
        h += self.contentsMargins().bottom()

        print(widget.height(), h)
        self.resize(self.width(), h)

    def insertWidget(self, index: int , widget: VWidget):
        widget.setParent(self)
        widget.resizeWidth(self.width() - self.contentsMargins().left() - self.contentsMargins().right())
        self.widgetList.insert(0, widget)
        self.updateHeight()

    def clear(self):
        for widget in self.widgetList:
            del widget

        self.widgetList.clear()
        self.spacing.clear()

    def updateHeight(self):
        h = self.contentsMargins().top()
        for i, widget in enumerate(self.widgetList):
            widget.resizeWidth(self.width() - self.contentsMargins().left() - self.contentsMargins().right())
            widget.move(self.contentsMargins().left(), h)
            h += widget.height()
            if i != len(self.widgetList) - 1:
                h += self.spacing[i]

        h += self.contentsMargins().bottom()

        self.resize(self.width(), h)

    def resizeWidth(self, w: int):
        h = self.contentsMargins().top()
        for i, widget in enumerate(self.widgetList):
            widget.resizeWidth(w - self.contentsMargins().left() - self.contentsMargins().right())
            widget.move(self.contentsMargins().left(), h)
            h += widget.height()
            if i != len(self.widgetList) - 1:
                h += self.spacing[i]

        h += self.contentsMargins().bottom()

        self.resize(w, h)







