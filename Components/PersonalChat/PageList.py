from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QPushButton
from PyQt6.QtCore import QObject, QMargins, Qt, pyqtBoundSignal, pyqtSignal, QPoint, QEvent
from PyQt6.QtGui import QCursor, QEnterEvent, QMoveEvent, QPalette, QColor, QResizeEvent, QColorConstants, QFont, QMouseEvent, QPaintEvent, QPainter, QColor, QBrush, QPen, QPainterPath

from .PageListButton import PageListButton
from ..Boxes.EmptyPage import EmptyPage
from .. import UiController


class PageListWorkZone(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)
        self.__centralWidget = EmptyPage(self)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.Green)
        self.setPalette(pal)

        lay = QGridLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(QMargins(0, 0, 0, 0))
        lay.addWidget(self.__centralWidget)

    def centralWidget(self):
        return self.__centralWidget

    def setCentralWidget(self, w: QWidget):
        if self.__centralWidget != None:
            self.__centralWidget.setEnabled(False)
            self.__centralWidget.hide()
            self.layout().removeWidget(self.__centralWidget)
        self.layout().addWidget(w)
        w.setEnabled(True)
        w.show()
        self.__centralWidget = w
        
    def resizeEvent(self, event: QResizeEvent) -> None:
        self.__centralWidget.move(0, 0)
        self.__centralWidget.resize(event.size())
        

class PageListButtonZone(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.setFixedHeight(40)

        empty = QWidget(self)

        self.lay = QHBoxLayout(self)
        self.lay.setSpacing(5)
        self.lay.setContentsMargins(QMargins(5, 5, 5, 5))
        self.lay.addStretch()
        self.setLayout(self.lay)
    
    def addButton(self, b: PageListButton):
        self.lay.insertWidget(0, b)


class PageList(QWidget):
    def __init__(self, parent: QObject | None = None):
        QWidget.__init__(self, parent)
        self.widgetList = []
        self.buttonList = []
        self.activeButton: PageListButton = None

        self.setMinimumSize(200, 200)

        self.buttonZone = PageListButtonZone(self)
        self.workZone = PageListWorkZone(self)

        lay = QVBoxLayout(self)
        lay.addWidget(self.buttonZone)
        lay.addWidget(self.workZone)
        lay.setContentsMargins(QMargins(0, 0, 0, 0))
        lay.setSpacing(0)
        self.setLayout(lay)

    def setActiveButton(self, i: int):
        b: PageListButton = self.buttonList[i]
        if (self.activeButton != b):
            if (self.activeButton != None):
                self.activeButton.setActive(False)
            self.activeButton = b
            b.setActive()

        b.up()

        self.workZone.setCentralWidget(b.widget)

    def addButton(self, name: str = "new Button", w: QWidget = None) -> PageListButton:
        button = PageListButton(name, w, self.buttonZone)
        button.setRadius(5)
        button.clicked.connect(self.setActiveButton)
        button.index = len(self.buttonList)
        self.buttonList.append(button)
        self.buttonZone.addButton(button)
        return button


    def addWidget(self, w: QWidget, name: str = "newPage"):
        self.widgetList.append(w)

        b = self.addButton(name, w)

        if len(self.widgetList) == 1:
            self.setActiveButton(0)
        else:
            w.setEnabled(False)
            w.hide()

        self.activeButton.up()

