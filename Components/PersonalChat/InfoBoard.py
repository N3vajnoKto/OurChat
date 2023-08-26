from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QMargins
from PyQt6.QtGui import QPalette, QResizeEvent, QColorConstants, QFont

from ..Boxes.Avatar import Avatar
from ..Boxes.ButtonBox import ButtonBox


class InfoBoard(QWidget):
    def __init__(self, name: str, parent=None):
        QWidget.__init__(self, parent)

        self.name = name
        self.ref = ButtonBox(self)
        self.avatarBox = QWidget(self.ref)
        self.avatar = Avatar(22, self.name, self.avatarBox)
        self.infoBox = QWidget(self.ref)
        self.info = QLabel(self.infoBox)
        self.subinfo = QLabel(self.infoBox)

        self.avatar.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.avatarBox.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.infoBox.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.info.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.subinfo.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)

        self.avatarBox.setFixedSize(self.height() + 10, self.height())
        self.avatarBox.move(0, 0)

        lay = QGridLayout()
        lay.setAlignment(self.avatar, Qt.AlignmentFlag.AlignCenter)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.addWidget(self.avatar)
        self.avatarBox.setLayout(lay)

        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColorConstants.White)
        self.setPalette(pal)

        self.info.setText(self.name)
        self.subinfo.setText("conecting...")
        self.info.setMargin(1)
        self.subinfo.setMargin(1)
        font = QFont("Open Sans", 10, QFont.Weight.Medium)
        self.info.setFont(font)
        self.info.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.subinfo.setFont(QFont("Open Sans", 10))
        self.subinfo.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        pal = self.subinfo.palette()
        pal.setColor(self.subinfo.foregroundRole(), QColorConstants.Gray)
        self.subinfo.setPalette(pal)

        lay = QVBoxLayout()
        lay.setSpacing(0)
        lay.setContentsMargins(QMargins(0, 7, 0, 7))
        lay.addWidget(self.info)
        lay.addWidget(self.subinfo)
        self.infoBox.setLayout(lay)

        lay = QHBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(0)
        lay.addWidget(self.avatarBox)
        lay.addWidget(self.infoBox)
        self.ref.setLayout(lay)

        lay = QHBoxLayout()
        lay.setContentsMargins(QMargins(0, 0, 0, 0))
        lay.setSpacing(0)
        lay.addWidget(self.ref)
        self.setLayout(lay)


    def setAvatarRadius(self, rad: int):
        self.avatar.setRadius(rad)


    def resizeEvent(self, event: QResizeEvent) -> None:
        self.avatarBox.setFixedSize(event.size().height() + 10, event.size().height())
        if self.height() < self.avatar.radius() * 2:
            self.avatar.hide()
            self.avatar.setDisabled(True)
        else:
            self.avatar.show()
            self.avatar.setEnabled(True)
