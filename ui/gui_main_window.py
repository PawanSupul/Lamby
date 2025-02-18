from PyQt5.QtWidgets import (QApplication, QStackedWidget, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
                             QWidget, QSizePolicy, QScrollArea, QLineEdit, QGraphicsOpacityEffect,
                             QButtonGroup, QCheckBox, QFrame)
from PyQt5.QtGui import QPixmap, QScreen, QMouseEvent, QGuiApplication, QImage, QFontMetrics, QFont, QIcon, QColor
from PyQt5.QtCore import (Qt, QRect, QSize, QTimer, QPropertyAnimation, QEasingCurve, QAbstractAnimation,
                          QThread, pyqtSignal)

from functools import partial

from ui.gui_login_screen import LoginScreen
from ui.gui_signup_screen import SignUpScreen
from ui.gui_load_screen import LoadScreen
from ui.gui_app_screen import AppScreen


class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Lamb conversationalist')
        self.setGeometry(100, 100, 1500, 800)
        self.setStyleSheet("background-color: #e2d9d2")
        self.default_pixmap = QPixmap('images/default_on_screen.png')
        self.clicked_button_id = None

        self.login_screen = LoginScreen(self.go_to_named_screen)

        self.signup_screen = SignUpScreen(self.go_to_named_screen)

        self.load_screen = LoadScreen(self.go_to_named_screen)

        self.app_screen = AppScreen(self.go_to_named_screen)
        self.app_screen.make_app_screen()

        self.addWidget(self.login_screen)
        self.addWidget(self.signup_screen)
        self.addWidget(self.load_screen)
        self.addWidget(self.app_screen)

        # self.load_screen.set_username('test')
        self.setCurrentWidget(self.login_screen)


    def go_to_named_screen(self, screen_name, **kwargs):
        if screen_name == 'login':
            self.login_screen.set_username(kwargs['username'])
            self.login_screen.initiation_protocol()
            self.setCurrentWidget(self.login_screen)
        elif(screen_name == 'signup'):
            self.setCurrentWidget(self.signup_screen)
        elif(screen_name == 'load'):
            self.load_screen.set_username(kwargs['username'])
            self.load_screen.initiation_protocol()
            self.setCurrentWidget(self.load_screen)
        elif(screen_name == 'app'):
            self.app_screen.set_information(kwargs['username'], lesson_num=kwargs['lesson_num'], lesson_description=kwargs['lesson'], mode=kwargs['mode'])
            self.setCurrentWidget(self.app_screen)
        else:
            self.setCurrentWidget(self.login_screen)

    # def go_to_app(self, username):
    #     self.app_screen.update_username(username)
    #     self.setCurrentWidget(self.app_screen)




