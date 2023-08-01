from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPalette, QColorConstants, QPaintEvent, QPainter, QBrush, QPen, QResizeEvent


class Avatar(QWidget):
    def __init__(self, rad: int = 20, parent=None):
        QWidget.__init__(self, parent)

        self.__radius = rad

        self.setFixedSize(2 * rad, 2 * rad)

    def radius(self):
        return self.__radius

    def setRadius(self, rad: int):
        self.__radius = rad
        self.setFixedSize(2 * rad, 2 * rad)

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(QColorConstants.Red))
        painter.setPen(QPen(QColorConstants.Transparent, 0))
        painter.drawRoundedRect(self.rect(), self.radius(), self.radius())
        super().paintEvent(event)

    
        

