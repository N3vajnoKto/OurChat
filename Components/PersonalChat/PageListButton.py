from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt6.QtCore import QObject, QMargins, Qt, pyqtBoundSignal, pyqtSignal, QPoint, QEvent
from PyQt6.QtGui import QCursor, QEnterEvent, QMoveEvent, QPalette, QColor, QResizeEvent, QColorConstants, QFont, QMouseEvent, QPaintEvent, QPainter, QColor, QBrush, QPen, QPainterPath

from .. import UiController

class PageListButton(QWidget):
    clicked = pyqtSignal(int)
    def __init__(self, name: str = "button", w: QWidget = None, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.name = name
        self.widget = w
        self.index = 0
        self.rad = 12

        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)


        self.curColor = QColorConstants.Transparent

        self.__active: bool = False

        self.setFixedWidth(100)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColorConstants.Transparent)
        self.setPalette(pal)

        self.label = QLabel(self)
        self.label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.label.setText(self.name)
        self.label.setFont(QFont(UiController.DefaultFontFamily, 10, QFont.Weight.Medium))

        lay = QGridLayout(self)
        lay.setContentsMargins(QMargins(0, 0, 0, 0))
        lay.setSpacing(0)
        lay.addWidget(self.label)
        lay.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def up(self):
        self.raise_()

    def setColor(self, c: QColor):
        self.curColor = c

    def radius(self) -> int:
        return self.rad

    def setRadius(self, r: int):
        self.rad = r

    def color(self) -> QColor:
        return self.curColor

    def setActive(self, b: bool = True):
        self.__active = b
        pal = self.label.palette()
        if (self.isActive()):
            self.setColor(UiController.ThemeColor)
            pal.setColor(self.label.foregroundRole(), QColorConstants.White)
        else:
            self.setColor(QColorConstants.White)
            pal.setColor(self.label.foregroundRole(), QColorConstants.Black)

        self.label.setPalette(pal)


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

        painter.drawRoundedRect(self.rect(), self.height() // 2, self.height() // 2)


    def resizeEvent(self, event: QResizeEvent) -> None:
        pass

    def enterEvent(self, event: QEnterEvent) -> None:
        if not self.isActive():
            self.setColor(UiController.HoverBackgroundColor)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        QWidget.enterEvent(self, event)

    def leaveEvent(self, event: QEvent) -> None:
        if not self.isActive():
            self.setColor(QColorConstants.Transparent)
        self.setCursor(Qt.CursorShape.ArrowCursor)
        QWidget.leaveEvent(self, event)