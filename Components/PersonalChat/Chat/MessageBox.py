from PyQt6.QtWidgets import QWidget, QTextEdit, QFrame
from PyQt6.QtCore import QObject, Qt, pyqtSignal
from PyQt6.QtGui import QColorConstants, QPen, QFont, QWheelEvent, QResizeEvent, QBrush, QFontMetrics, QPainter, QPaintEvent, QPainterPath

from ...Boxes.ScrollStack import ScrollStack

class MessageBox(QWidget):
    def __init__(self, text: str, b: bool = False, parent: QObject = None):
        QWidget.__init__(self, parent)

        self.marginX = 5
        self.marginY = 2

        self.mine: bool = b

        self.message = Message(text, b, self)

        if self.mine:
            self.message.move(self.width() - self.message.width() - self.marginX, self.marginY)
        else:
            self.message.move(self.marginX, self.marginY)

        self.setFixedHeight(self.message.height() + 2 * self.marginY)

    def mine(self):
        return self.mine

    def setMine(self, b: bool):
        self.mine = b
        if self.mine:
            self.message.move(self.width() - self.message.width() - self.marginX, self.marginY)
        else:
            self.message.move(self.marginX, self.marginY)

    def resizeEvent(self, event: QResizeEvent) -> None:
        if self.mine:
            self.message.move(self.width() - self.message.width() - self.marginX, self.marginY)
        else:
            self.message.move(self.marginX, self.marginY)

    def wheelEvent(self, e: QWheelEvent) -> None:
        e.ignore()


class MyTextEdit(QTextEdit):
    def __init__(self, text: str, parent: QObject = None):
        QTextEdit.__init__(self, text, parent)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def wheelEvent(self, e: QWheelEvent) -> None:
        e.ignore()


class Message(QWidget):
    def __init__(self, text: str, b: bool = False, parent: QObject = None):
        QWidget.__init__(self, parent)

        self.setMaximumWidth(300)
        self.marginX = 5
        self.marginY = 5
        self.mine = b
        self.rad = 10

        self.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.text = MyTextEdit(text, self)
        self.text.setLineWrapMode(QTextEdit.LineWrapMode.FixedPixelWidth)
        self.text.setFrameShape(QFrame.Shape.NoFrame)
        self.text.setFont(QFont("Open Sans", 10))
        self.text.setReadOnly(True)
        self.text.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.text.move(self.marginX + self.rad, self.marginY)

        m = QFontMetrics(self.text.font())
        w = int(m.boundingRect(self.text.toPlainText()).width())
        nw = self.maximumWidth() - 2 * self.marginX - 2 * self.rad
        if w + 10 < nw:
            nw = w + 10

        self.text.resize(nw, self.text.height())
        self.text.setLineWrapColumnOrWidth(self.text.width())

        self.text.resize(int(self.text.document().size().width()), int(self.text.document().size().height()))

        self.setFixedSize(self.text.width() + 2 * self.marginX + 2 * self.rad, self.text.height() + 2 * self.marginY)



    def mine(self):
        return self.mine

    def setMine(self, b: bool):
        self.mine = b

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        painter.setBrush(QBrush(QColorConstants.White))
        painter.setPen(QPen(QColorConstants.Transparent))

        path = QPainterPath()

        r = self.rad
        d = 2 * r


        if not self.mine:
            path.moveTo(0, self.height())
            path.arcTo(-r, self.height() - d, d, d, 270, 90)
            path.lineTo(r, r)
            path.arcTo(r, 0, d, d, 180, -90)
            path.lineTo(self.width() - d, 0)
            path.arcTo(self.width() - 3 * r, 0, d, d, 90, -90)
            path.lineTo(self.width() - r, self.height() - r)
            path.arcTo(self.width() - 3 *  r, self.height() - d, d, d, 0, -90)
            path.closeSubpath()
        else:
            path.moveTo(self.width(), self.height())
            path.arcTo(self.width() - r, self.height() - d, d, d, 270, -90)
            path.lineTo(self.width() - r, r)
            path.arcTo(self.width() - 3 * r, 0, d, d, 0, 90)
            path.lineTo(d, 0)
            path.arcTo(r, 0, d, d, 90, 90)
            path.lineTo(r, self.height() - r)
            path.arcTo(r, self.height() - d, d, d, 180, 90)
            path.closeSubpath()

        painter.drawPath(path)

    def wheelEvent(self, e: QWheelEvent) -> None:
        e.ignore()








