import copy

from PyQt6.QtWidgets import QWidget, QTextEdit, QFrame, QLabel
from PyQt6.QtCore import QObject, Qt, pyqtSignal, QMargins, QSize
from PyQt6.QtGui import QColorConstants, QPalette, QPen, QFont, QWheelEvent, QResizeEvent, QBrush, QFontMetrics, QPainter, \
    QPaintEvent, QPainterPath

from .MessageInfo import MessageInfo, MessageInfoBox
from ... import UiController


class MyTextEdit(QTextEdit):
    def __init__(self, text: str, parent: QObject | None = None):
        QTextEdit.__init__(self, text, parent)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Base, QColorConstants.Transparent)
        self.setPalette(pal)

    def wheelEvent(self, e: QWheelEvent) -> None:
        e.ignore()

class Message(QWidget):
    def __init__(self, info: MessageInfo, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.setMaximumWidth(300)
        self.margins = QMargins(8, 3, 8, 3)
        self.info = info
        self.spacingX = 0
        self.spacingY = -18

        self.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.text = MyTextEdit(self.info.text, self)
        self.text.setLineWrapMode(QTextEdit.LineWrapMode.FixedPixelWidth)
        self.text.setFrameShape(QFrame.Shape.NoFrame)
        self.text.setFont(QFont(UiController.DefaultFontFamily, 10))
        self.text.setReadOnly(True)
        self.text.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.infoBox = MessageInfoBox(self.info, self)

        self.format()

    def isMine(self):
        return self.info.mine

    def setMine(self, b: bool):
        self.info.mine = b

    def format(self) -> QSize:
        m = QFontMetrics(self.text.font())
        self.text.move(self.margins.left(), self.margins.top())

        w = int(m.boundingRect(self.text.toPlainText()).width())
        nw = self.maximumWidth() - self.margins.left() - self.margins.right()
        if w + 10 < nw:
            nw = w + 10

        self.text.resize(nw, self.text.height())
        self.text.setLineWrapColumnOrWidth(self.text.width())

        self.text.resize(int(self.text.document().size().width()), int(self.text.document().size().height()))

        if self.infoBox.width() + self.text.width() + self.spacingX <= self.maximumWidth() - self.margins.left() - self.margins.right():
            w = self.text.width() + self.infoBox.width() + self.margins.left() + self.margins.right() + self.spacingX
            h = self.text.height() + self.margins.top() + self.margins.bottom()
            self.setFixedSize(w, h)
            self.infoBox.move(self.margins.left() + self.text.width() + self.spacingX,
                              self.margins.top() + self.text.height() + self.spacingY)
        else:
            w = self.text.width() + self.margins.left() + self.margins.right()
            h = self.text.height() + self.margins.top() + self.margins.bottom() + self.infoBox.height()
            self.setFixedSize(w, h)
            self.infoBox.move(self.margins.left() + self.text.width() - self.infoBox.width(),
                              self.margins.top() + self.text.height())

        return self.size()

    def wheelEvent(self, e: QWheelEvent) -> None:
        e.ignore()
