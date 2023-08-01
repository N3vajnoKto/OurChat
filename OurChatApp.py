from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QFontDatabase, QFont
from Components.OurChat import OurChat

from Components.Fonts import font_src

import sys

app = QApplication(sys.argv)
QFontDatabase.addApplicationFont(":/Open_Sans/OpenSans-Regular.ttf")
QFontDatabase.addApplicationFont(":/Open_Sans/OpenSans-Bold.ttf")

chat = OurChat()
chat.show()

app.exec()
