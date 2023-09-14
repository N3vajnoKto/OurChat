from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QFontDatabase, QFont
import sys

from Components.OurChat import OurChat
from Components import UiController
from Components.Back_End.Application import Application
from Components.Back_End import ApplicationController
from Components.Back_End.Account import Account
from Components.Back_End.Chat import Chat


app = QApplication(sys.argv)
QFontDatabase.addApplicationFont("Components/Resources/Fonts/Open_Sans/OpenSans-Regular.ttf")
QFontDatabase.addApplicationFont("Components/Resources/Fonts/Open_Sans/OpenSans-Bold.ttf")
QFontDatabase.addApplicationFont("Components/Resources/Fonts/Open_Sans/OpenSans-Light.ttf")
QFontDatabase.addApplicationFont("Components/Resources/Fonts/Open_Sans/OpenSans-Medium.ttf")

application = Application()

for i in range(50):
    application.addChat(Chat(Account()))

application.addAccount(Account())
application.addAccount(Account())
application.addAccount(Account())

application.setCurrentIndex(0)

chat = OurChat()

chat.show()

app.exec()
