from PyQt6.QtWidgets import QWidget, QTextEdit, QFrame, QLabel
from PyQt6.QtCore import QObject, Qt, pyqtSignal, QMargins, QSize
from PyQt6.QtGui import QColorConstants, QPen, QFont, QWheelEvent, QResizeEvent, QBrush, QMoveEvent, QPainter, \
    QPaintEvent, QPainterPath

from typing import Self

from .Message import Message
from .MessageInfo import MessageInfo
from ...Boxes.VWidget import VWidget


class MessageBox(VWidget):
    def __init__(self, info: MessageInfo, parent: QObject | None = None):
        VWidget.__init__(self, parent)

        self.connectMargins: QMargins = QMargins(2, 1, 2, 0)
        self.disconnectMargins: QMargins = QMargins(2, 5, 2, 0)
        self.margins: QMargins = self.disconnectMargins

        self.messageFrame = MessageFrame(None, self)
        self.message = Message(info, self)

        self.messageFrame.setMessage(self.message)
        self.message.setMaximumWidth(self.maxWidth())

        # self.setAutoFillBackground(True)
        # pal = self.palette()
        # pal.setColor(self.backgroundRole(), QColorConstants.Green)
        # self.setPalette(pal)

        self.arrange()

    def arrange(self):
        if (self.message.info.isConnectedFromTop()):
            self.margins.setTop(self.connectMargins.top())
        else:
            self.margins.setTop(self.disconnectMargins.top())

        if (self.message.info.isConnectedFromBottom()):
            self.margins.setBottom(self.connectMargins.bottom())
        else:
            self.margins.setBottom(self.disconnectMargins.bottom())


        if (self.messageFrame.height() + self.margins.top() + self.margins.bottom() != self.height()):
            self.setFixedHeight(self.messageFrame.height() + self.margins.top() + self.margins.bottom())

        if self.message.info.mine:
            self.messageFrame.move(self.width() - self.messageFrame.width() - self.margins.right(),
                              self.margins.top())
        else:
            self.messageFrame.move(self.margins.left(), self.margins.top())

    def maxWidth(self):
        return min(450, int(0.7 * self.width()))

    def connectMessage(self, other: Self):
        if other is None:
            return
        self.message.info.connectTop(other.message.info)
        self.messageFrame.update()
        other.messageFrame.update()
        self.arrange()
        other.arrange()

    def resizeWidth(self, w: int):
        self.resize(w, self.height())
        self.message.setMaximumWidth(self.maxWidth())
        self.message.format()
        self.messageFrame.updateSize()
        self.arrange()

    def mine(self):
        return self.message.info.mine

    def setMine(self, b: bool):
        self.message.setMine(b)

        self.arrange()

    def resizeEvent(self, event: QResizeEvent) -> None:
        if event.oldSize().width() != event.size().width():
            self.arrange()

    def wheelEvent(self, e: QWheelEvent) -> None:
        e.ignore()

    def setMargins(self, left: int, top: int, right: int, bottom: int):
        self.margins.setLeft(left)
        self.margins.setTop(top)
        self.margins.setRight(right)
        self.margins.setBottom(bottom)
        self.arrange()

    def setMarginLeft(self, left: int):
        self.margins.setLeft(left)
        self.arrange()

    def setMarginTop(self, top: int):
        self.margins.setTop(top)
        self.arrange()

    def setMarginRight(self, right: int):
        self.margins.setRight(right)
        self.arrange()

    def setMarginBottom(self, bottom: int):
        self.margins.setBottom(bottom)
        self.arrange()

    def moveEvent(self, event:  QMoveEvent) -> None:
        pass


class MessageFrame(QWidget):
    count: int = 0
    def __init__(self, message: Message = None, parent: QObject | None = None):
        QWidget.__init__(self, parent)
        self.message = message
        if self.message is not None:
            self.message.setParent(self)

        self.tailWidth: int = 6
        self.borderRadius = 16
        self.borderConnectedRadius = 6
        self.tailHeight = 10

        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

    def setMessage(self, message: Message):
        self.message = message
        self.message.setParent(self)
        self.format()
        self.updateSize()

    def format(self):
        if (self.message.isMine()):
            self.message.move(0, 0)
        else:
            self.message.move(self.tailWidth, 0)

        self.update()

    def updateSize(self) -> None:
        if self.message is not None:
            if self.size() != QSize(self.message.width() + self.tailWidth, self.message.height()):
                self.resize(QSize(self.message.width() + self.tailWidth, self.message.height()))

        self.format()

    def paintEvent(self, event: QPaintEvent) -> None:
        if self.message is None:
            return

        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setBrush(QBrush(QColorConstants.White))
        painter.setPen(QPen(QColorConstants.Transparent))

        path = QPainterPath()

        r = self.borderRadius
        cr = self. borderConnectedRadius
        d = 2 * r
        cd = cr * 2

        tw = self.tailWidth
        th = self.tailHeight

        cf = 1
        if not self.message.info.mine:
            path.moveTo(2, self.height())
            if self.message.info.isConnectedFromBottom():
                path.arcTo(tw, self.height() - cd, cd, cd, 270, -90)
            else:
                path.arcTo(-tw, self.height() - 2 * th - cf, 2 * tw, 2 * th, 280, 80)

            if self.message.info.isConnectedFromTop():
                path.lineTo(tw, cr)
                path.arcTo(tw, 0, cd, cd, 180, -90)
            else:
                path.lineTo(tw, r)
                path.arcTo(tw, 0, d, d, 180, -90)

            path.lineTo(self.width() - r, 0)
            path.arcTo(self.width() - d, 0, d, d, 90, -90)
            path.lineTo(self.width(), self.height() - r)
            path.arcTo(self.width() - d, self.height() - d, d, d, 0, -90)

            path.closeSubpath()
        else:
            path.moveTo(self.width() - 2, self.height())
            if self.message.info.isConnectedFromBottom():
                path.arcTo(self.width() - tw - cd, self.height() - cd, cd, cd, 270, 90)
            else:
                path.arcTo(self.width() - tw, self.height() - 2 * th - cf, 2 * tw, 2 * th, 260, -80)

            if self.message.info.isConnectedFromTop():
                path.lineTo(self.width() - tw, cr)
                path.arcTo(self.width() - cd - tw, 0, cd, cd, 0, 90)
            else:
                path.lineTo(self.width() - tw, r)
                path.arcTo(self.width() - d - tw, 0, d, d, 0, 90)
            path.lineTo(r, 0)
            path.arcTo(0, 0, d, d, 90, 90)
            path.lineTo(0, self.height() - r)
            path.arcTo(0, self.height() - d, d, d, 180, 90)
            path.closeSubpath()

        painter.drawPath(path)

    def wheelEvent(self, event: QWheelEvent) -> None:
        event.ignore()

