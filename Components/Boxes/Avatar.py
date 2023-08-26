from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout
from PyQt6.QtGui import QColorConstants, QPaintEvent, QPainter, QBrush, QPen, QResizeEvent, QImage, QColor, QLinearGradient, QFont
from PyQt6.QtCore import Qt
from random import randint

class Avatar(QWidget):
    def __init__(self, rad: int = 22, nm: str = "E", parent=None):
        QWidget.__init__(self, parent)

        self.__radius = rad
        self.img: QImage = None
        self.name: str = nm

        self.letter = QLabel(self)
        self.letter.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.letter.setText(self.name[0])
        self.letter.setFont(QFont("Open Sans", rad, QFont.Weight.Medium))
        
        pal = self.letter.palette()
        pal.setColor(self.letter.foregroundRole(), QColorConstants.White)
        self.letter.setPalette(pal)

        lay = QGridLayout(self)
        lay.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lay.addWidget(self.letter)
        self.setLayout(lay)

        if self.img != None:
            self.letter.hide()
            self.letter.setDisabled(True)

        self.bckColor: QColor = QColor.fromHsv(randint(0, 359), randint(200, 255), randint(220, 240))

        self.setFixedSize(2 * rad, 2 * rad)

    def setImage(self, p: QImage):
        self.img = p
        if self.img != None:
            self.letter.hide()
            self.letter.setDisabled(True)

    def image(self):
        return self.img

    def radius(self):
        return self.__radius

    def setRadius(self, rad: int):
        self.__radius = rad
        self.setFixedSize(2 * rad, 2 * rad)

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)

        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        if (self.img != None):
            painter.setBrush(QBrush(self.img))
        else:
            g = QLinearGradient(0, 0, self.width(), self.height())
            fc = QColor.fromHsv(self.bckColor.hslHue(), self.bckColor.hsvSaturation() - 120, self.bckColor.value())
            g.setColorAt(0, fc)
            g.setColorAt(1, self.bckColor)
            painter.setBrush(QBrush(g))
        painter.setPen(QPen(QColorConstants.Transparent, 0))
        painter.drawRoundedRect(self.rect(), self.radius(), self.radius())
        painter.setPen(QPen(QColorConstants.White, 0))
        super().paintEvent(event)

    
        

