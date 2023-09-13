from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt6.QtCore import QObject, QMargins, Qt, pyqtBoundSignal, pyqtSignal, QPoint, QEvent
from PyQt6.QtGui import QCursor, QEnterEvent, QMoveEvent, QPalette, QColor, QResizeEvent, QColorConstants, QFont, QMouseEvent, QPaintEvent, QPainter, QColor, QBrush, QPen, QPainterPath

from .. import UiController


class Neighbour(QWidget):
    def __init__(self, w: int, parent: QObject | None = None):
        QWidget.__init__(self, parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        
        self.color: QColor = QColorConstants.Transparent
        self.where = w
        self.rad = 12

    def isLeft(self):
        return self.where == 0

    def isRight(self):
        return self.where == 1

    def setColor(self, c: QColor):
        self.color = c

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(self.color))
        painter.setPen(QPen(QColorConstants.Transparent, 0))

        path = QPainterPath()

        if (self.isLeft()):
            path.moveTo(self.width(), self.height() - self.rad * 2)
            path.arcTo(self.width() - self.rad * 2, self.height() - self.rad * 2, self.rad * 2, self.rad * 2, 0, -90)
            path.lineTo(self.width(), self.height())
            path.closeSubpath()
        else:
            path.moveTo(0, self.height() - self.rad * 2)
            path.arcTo(0, self.height() - self.rad * 2 ,self.rad * 2, self.rad * 2, 180, 90)
            path.lineTo(0, self.height())
            path.closeSubpath()

        painter.drawPath(path)


class PageListButton(QWidget):
    clicked = pyqtSignal(int)
    def __init__(self, name: str = "button", w: QWidget = None, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.name = name
        self.widget = w
        self.index = 0
        self.rad = 12

        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)

        self.left: Neighbour = Neighbour(0, parent)
        self.right: Neighbour = Neighbour(1, parent)

        self.bckDef = QColorConstants.Transparent
        self.bckHover = QColorConstants.Red
        self.bckActive = QColorConstants.Blue

        self.curColor = self.bckDef

        self.__active: bool = False

        self.setFixedSize(100, 30)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColorConstants.Transparent)
        self.setPalette(pal)

        self.label = QLabel(self)
        self.label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.label.setText(self.name)
        self.label.setFont(QFont(UiController.DefaultFontFamily, 10, QFont.Weight.Medium))

        lay = QGridLayout(self)
        lay.setContentsMargins(QMargins(5, 0, 5, 0))
        lay.setSpacing(0)
        lay.addWidget(self.label)
        lay.setAlignment(Qt.AlignmentFlag.AlignVCenter)

    def up(self):
        self.left.raise_()
        self.right.raise_()
        self.raise_()

    def setColor(self, c: QColor):
        self.curColor = c
        self.left.color = c
        self.right.color = c

    def radius(self) -> int:
        return self.rad

    def setRadius(self, r: int):
        self.rad = r
        self.left.rad = r + 1
        self.right.rad = r + 1

    def color(self) -> QColor:
        return self.curColor

    def setActive(self, b: bool = True):
        self.__active = b
        if (self.isActive()):
            self.setColor(self.bckActive)
        else:
            self.setColor(self.bckDef)
        self.update()

    def isActive(self) -> bool:
        return self.__active

    def mousePressEvent(self, event: QMouseEvent) -> None:
        if event.button() == Qt.MouseButton.LeftButton and not self.isActive():
            self.clicked.emit(self.index)

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(self.curColor))
        painter.setPen(QPen(QColorConstants.Transparent, 0))

        path = QPainterPath()

        path.moveTo(0, self.height())
        path.lineTo(0, self.rad * 2)
        path.arcTo(0, 0, self.rad * 2, self.rad * 2, 180, -90)
        path.lineTo(self.width() - self.rad * 2, 0)
        path.arcTo(self.width() - self.rad * 2, 0, self.rad * 2, self.rad * 2, 90, -90)
        path.lineTo(self.width(), self.height())
        path.closeSubpath()

        painter.drawPath(path)

        self.left.update()
        self.right.update()

    def moveEvent(self, event: QMoveEvent) -> None:
        self.left.move(event.pos() - QPoint(self.left.width() - 1, 0))
        self.right.move(event.pos() + QPoint(self.width() - 1, 0))


    def resizeEvent(self, event: QResizeEvent) -> None:
        self.left.resize(event.size().height(), event.size().height())
        self.right.resize(event.size().height(), event.size().height())
        self.left.move(self.pos() - QPoint(self.left.width() - 1, 0))
        self.right.move(self.pos() + QPoint(self.width() - 1, 0))

    def enterEvent(self, event: QEnterEvent) -> None:
        if not self.isActive():
            self.setColor(self.bckHover)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        QWidget.enterEvent(self, event)

    def leaveEvent(self, event: QEvent) -> None:
        if not self.isActive():
            self.setColor(self.bckDef)
        self.setCursor(Qt.CursorShape.ArrowCursor)
        QWidget.leaveEvent(self, event)