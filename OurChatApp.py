from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QFontDatabase, QFont
import sys

from Components.OurChat import OurChat

from Components.Fonts import font_src


app = QApplication(sys.argv)
QFontDatabase.addApplicationFont(":/Open_Sans/OpenSans-Regular.ttf")
QFontDatabase.addApplicationFont(":/Open_Sans/OpenSans-Bold.ttf")
QFontDatabase.addApplicationFont(":/Open_Sans/OpenSans-Light.ttf")
QFontDatabase.addApplicationFont(":/Open_Sans/OpenSans-Medium.ttf")

chat = OurChat()
chat.show()

app.exec()
