from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QMargins
from PyQt6.QtGui import QPalette, QResizeEvent, QColorConstants, QFont
from ..Avatar import Avatar


class InfoBoard(QWidget):
    def __init__(self, name: str, parent=None):
        QWidget.__init__(self, parent)

        self.name = name
        self.avatarBox = QWidget(self)
        self.avatar = Avatar(25, self.avatarBox)
        self.infoBox = QWidget(self)
        self.info = QLabel(self)
        self.subinfo = QLabel(self)

        lay = QHBoxLayout(self)
        lay.setContentsMargins(QMargins(5, 0, 5, 0))
        lay.setSpacing(0)
        lay.addWidget(self.avatarBox)
        lay.addWidget(self.infoBox)
        self.setLayout(lay)

        self.avatarBox.setFixedSize(self.height(), self.height())
        self.avatarBox.move(0, 0)

        lay = QGridLayout(self.avatarBox)
        lay.setAlignment(self.avatar, Qt.AlignmentFlag.AlignCenter)
        lay.setContentsMargins(QMargins(0, 0, 0, 0))
        lay.addWidget(self.avatar)
        self.avatarBox.setLayout(lay)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColorConstants.White)
        self.setPalette(pal)

        self.info.setText(self.name)
        self.subinfo.setText(self.name)
        font = QFont("Open Sans", 11)
        self.info.setFont(font)
        self.info
        self.info.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.subinfo.setFont(QFont("Open Sans", 11))
        self.subinfo.setAlignment(Qt.AlignmentFlag.AlignTop)
        pal = self.subinfo.palette()
        pal.setColor(self.subinfo.foregroundRole(), QColorConstants.Gray)
        self.subinfo.setPalette(pal)

        # pal = self.info.palette()
        # self.info.setAutoFillBackground(True)
        # pal.setColor(self.info.backgroundRole(), QColorConstants.Green)
        # self.info.setPalette(pal)

        # pal = self.subinfo.palette()
        # self.subinfo.setAutoFillBackground(True)
        # pal.setColor(self.subinfo.backgroundRole(), QColorConstants.Red)
        # self.subinfo.setPalette(pal)

        lay = QVBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(QMargins(0, 10, 0, 10))
        lay.addWidget(self.info)
        lay.addWidget(self.subinfo)
        self.infoBox.setLayout(lay)


    def setAvatarRadius(self, rad: int):
        self.avatar.setRadius(rad)


    def resizeEvent(self, event: QResizeEvent) -> None:
        self.avatarBox.setFixedSize(event.size().height(), event.size().height())
        if self.height() < self.avatar.radius() * 2:
            self.avatar.hide()
            self.avatar.setDisabled(True)
        else:
            self.avatar.show()
            self.avatar.setEnabled(True)
