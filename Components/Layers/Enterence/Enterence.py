from typing import Optional
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout
from PyQt6.QtCore import QObject, Qt, pyqtSignal, QEvent, pyqtSlot
from PyQt6.QtGui import QPalette, QColor, QColorConstants, QResizeEvent, QFont, QIcon

from ... import UiController
from ...Boxes.InputLine import InputLine
from ...Boxes.ButtonBox import ButtonBox
from ...Boxes.TextLine import TextLine
from ...Boxes.IconButton import IconButton

class LogInField(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        QWidget.__init__(self, parent)

        self.title = TextLine("Log in", self)
        pal = self.title.palette()
        pal.setColor(self.title.foregroundRole(), UiController.DarkThemeColor)
        self.title.setPalette(pal)
        self.title.setFont(QFont(UiController.DefaultFontFamily, 20))
        self.title.setFixedHeight(50)

        self.login = InputLine(self)
        self.login.setPlaceholderText("login")

        self.password = InputLine(self)
        self.password.setPlaceholderText("password")

        self.loginButton = ButtonBox(self)
        self.loginButton.setFixedHeight(40)
        self.loginText = TextLine("log in", self.loginButton)
        lay = QGridLayout(self.loginButton)
        lay.addWidget(self.loginText)

        self.loginButton.setLayout(lay)

        self.registerButton = ButtonBox(self)
        self.loginButton.setFixedHeight(40)
        self.registerText = TextLine("register", self.registerButton)
        lay = QGridLayout(self.registerButton)
        lay.addWidget(self.registerText)

        self.registerButton.setLayout(lay)


        lay = QVBoxLayout(self)

        lay.setSpacing(5)
        lay.setContentsMargins(0, 0, 0, 0)

        lay.addWidget(self.title)
        lay.addWidget(self.login)
        lay.addWidget(self.password)

        hlay = QHBoxLayout(self)

        hlay.setSpacing(5)
        hlay.setContentsMargins(0, 0, 0, 0)
        hlay.addWidget(self.loginButton)
        hlay.addStretch()
        hlay.addWidget(self.registerButton)

        hlay.setAlignment(self.loginText, Qt.AlignmentFlag.AlignLeft)
        hlay.setAlignment(self.registerText, Qt.AlignmentFlag.AlignRight)

        lay.addLayout(hlay)

        lay.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(lay)


class RegisterField(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        QWidget.__init__(self, parent)

        self.title = TextLine("Register", self)
        pal = self.title.palette()
        pal.setColor(self.title.foregroundRole(), UiController.DarkThemeColor)
        self.title.setPalette(pal)
        self.title.setFont(QFont(UiController.DefaultFontFamily, 20))
        self.title.setFixedHeight(50)

        self.login = InputLine(self)
        self.login.setPlaceholderText("login")

        self.password = InputLine(self)
        self.password.setPlaceholderText("password")

        self.repPassword = InputLine(self)
        self.repPassword.setPlaceholderText("repeat the password")

        self.loginButton = ButtonBox(self)
        self.loginButton.setFixedHeight(40)
        self.loginText = TextLine("log in", self.loginButton)
        lay = QGridLayout(self.loginButton)
        lay.addWidget(self.loginText)

        self.loginButton.setLayout(lay)

        self.registerButton = ButtonBox(self)
        self.loginButton.setFixedHeight(40)
        self.registerText = TextLine("register", self.registerButton)
        lay = QGridLayout(self.registerButton)
        lay.addWidget(self.registerText)

        self.registerButton.setLayout(lay)

        lay = QVBoxLayout(self)

        lay.setSpacing(5)
        lay.setContentsMargins(0, 0, 0, 0)

        lay.addWidget(self.title)
        lay.addWidget(self.login)
        lay.addWidget(self.password)
        lay.addWidget(self.repPassword)

        hlay = QHBoxLayout(self)

        hlay.setSpacing(5)
        hlay.setContentsMargins(0, 0, 0, 0)
        hlay.addWidget(self.loginButton)
        hlay.addStretch()
        hlay.addWidget(self.registerButton)

        hlay.setAlignment(self.loginText, Qt.AlignmentFlag.AlignLeft)
        hlay.setAlignment(self.registerText, Qt.AlignmentFlag.AlignRight)

        lay.addLayout(hlay)

        lay.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.setLayout(lay)


class Enterence(QWidget):
    def __init__(self, parent: Optional[QWidget] = None):
        QWidget.__init__(self, parent)

        self.setAutoFillBackground(True)

        pal = self.palette()
        pal.setColor(self.backgroundRole(), UiController.Light)
        self.setPalette(pal)

        self.setContentsMargins(5, 5, 5, 5)

        self.backButton = IconButton(QIcon("Components/Resources/Icons/back_arrow.svg"), self)

        self.backButton.move(self.contentsMargins().left(), self.contentsMargins().top())
        self.backButton.resize(25, 25)

        self.backButton.clicked.connect(UiController.Chat.focusMainPage)

        self.loginField = LogInField(self)

        self.loginField.setFixedSize(UiController.MinimumApplicationSize)

        self.registerField = RegisterField(self)
        self.registerField.hide()

        self.registerField.setFixedSize(UiController.MinimumApplicationSize)

        self.lay = QGridLayout(self)
        self.lay.setSpacing(0)
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.addWidget(self.loginField)

        self.setLayout(self.lay)

        self.loginField.registerButton.clicked.connect(self.openRegistration)
        self.registerField.loginButton.clicked.connect(self.openLogin)

    @pyqtSlot()
    def openRegistration(self):
        self.lay.removeWidget(self.loginField)
        self.loginField.hide()
        self.lay.addWidget(self.registerField)
        self.registerField.show()

    @pyqtSlot()
    def openLogin(self):
        self.lay.removeWidget(self.registerField)
        self.registerField.hide()
        self.lay.addWidget(self.loginField)
        self.loginField.show()

