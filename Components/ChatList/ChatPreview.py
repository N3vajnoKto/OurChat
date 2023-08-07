from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel
from PyQt6.QtCore import Qt, QObject, QEvent
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QResizeEvent, QEnterEvent, QFont

from ..Avatar import Avatar

class ChatPreview(QWidget):
    def __init__(self, name: str = "SomeOne", parent: QObject = None):
        QWidget.__init__(self, parent)

        self.setFixedHeight(54)

        self.setAttribute(Qt.WidgetAttribute.WA_Hover)

        self.setAutoFillBackground(True)

        self.setMouseTracking(True)

        self.setCursor(Qt.CursorShape.PointingHandCursor)

        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColorConstants.White)
        self.setPalette(pal)

        self.name = name
        self.defColor: QColor = QColorConstants.White
        self.avatarBox = QWidget(self)
        self.infoBox = QWidget(self)
        self.info = QLabel(self)
        self.subinfo = QLabel(self)
        self.avatar = Avatar(22, name, self.avatarBox)

        self.info.setFont(QFont("Open Sans", 10, QFont.Weight.Medium))
        self.info.setText(self.name)
        self.info.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        lay = QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 7, 0, 7)
        lay.addWidget(self.info)
        lay.addWidget(self.subinfo)
        self.infoBox.setLayout(lay)

        self.avatarBox.setFixedSize(self.height() + 10, self.height())

        lay = QGridLayout(self.avatarBox)
        lay.setAlignment(self.avatar, Qt.AlignmentFlag.AlignCenter)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.avatar)
        self.avatarBox.setLayout(lay)

        lay = QHBoxLayout(self)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        lay.addWidget(self.avatarBox)
        lay.addWidget(self.infoBox)
        self.setLayout(lay)

    def setBColor(self, c: QColor):
        pal = self.palette()
        pal.setColor(self.backgroundRole(), c)
        self.setPalette(pal)

    def enterEvent(self, event: QEnterEvent) -> None:
        self.setBColor(QColorConstants.Gray)
        self.update()

    def leaveEvent(self, event: QEvent) -> None:
        self.setBColor(self.defColor)
        self.update()