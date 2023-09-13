from typing import Optional
from enum import Enum

from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout
from PyQt6.QtCore import Qt, QObject
from PyQt6.QtGui import QColorConstants, QPaintEvent, QPainter, QBrush, QPen, QResizeEvent, QImage, QColor, \
    QLinearGradient, QFont, QFontMetrics

from ..Back_End.Account import *
from .. import UiController


class Avatar(QWidget):
    class AvatarForm(Enum):
        Rectangle = 0
        Rounded = 1

    def __init__(self, acc: Account, parent: QObject | None = None):
        QWidget.__init__(self, parent)

        self.account = acc

        self.form: Avatar.AvatarForm = Avatar.AvatarForm.Rounded

        self.setFont(UiController.DefaultFont)

        self.metrics: QFontMetrics = QFontMetrics(self.font())

    def setAvatarRadius(self, rad: int):
        self.setFixedSize(rad * 2, rad * 2)

    def setForm(self, f: AvatarForm):
        self.form = f

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.setFont(QFont(UiController.DefaultFontFamily, min(int(self.height() * 0.5), 35), QFont.Weight.Medium))
        self.metrics = QFontMetrics(self.font())

    def setAccount(self, acc: Account):
        self.account = acc

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)

        rad = self.height() // 2

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        if self.account.avatar() is not None:
            painter.setBrush(QBrush(self.account.avatar()))
        else:
            g = QLinearGradient(0, 0, self.width(), self.height())
            bkc = self.account.backgroundColor()
            fc = QColor.fromHsv(bkc.hslHue(), bkc.hsvSaturation() - 120, bkc.value())
            g.setColorAt(0, fc)
            g.setColorAt(1, bkc)
            painter.setBrush(QBrush(g))
        painter.setPen(QPen(QColorConstants.Transparent, 0))
        if self.form == Avatar.AvatarForm.Rounded:
            painter.drawRoundedRect(self.rect(), rad, rad)

        if self.form == Avatar.AvatarForm.Rectangle:
            painter.drawRect(self.rect())

        painter.setPen(QPen(QColorConstants.White, 0))
        letter = self.account.name()[0]
        painter.setFont(self.font())
        if self.form == Avatar.AvatarForm.Rectangle:
            print(self.metrics.height())
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, letter)
