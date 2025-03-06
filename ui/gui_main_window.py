from PyQt6.QtWidgets import QStackedWidget
from PyQt6.QtGui import QPixmap

from ui.gui_login_screen import LoginScreen
from ui.gui_signup_screen import SignUpScreen
from ui.gui_forget_screen import ForgotScreen
from ui.gui_load_screen import LoadScreen
from ui.gui_app_screen import AppScreen


class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__(None)
        self.setWindowTitle('Lamb conversationalist')
        self.setGeometry(100, 100, 1400, 700)
        self.setStyleSheet("background-color: #F2EED0")  #e2d9d2
        self.default_pixmap = QPixmap('images/default_on_screen.png')
        self.clicked_button_id = None

        self.login_screen = LoginScreen(self.go_to_named_screen)
        self.signup_screen = SignUpScreen(self.go_to_named_screen)
        self.forgot_screen = ForgotScreen(self.go_to_named_screen)
        self.load_screen = LoadScreen(self.go_to_named_screen)
        self.app_screen = AppScreen(self.go_to_named_screen)
        self.app_screen.make_app_screen()

        self.addWidget(self.login_screen)
        self.addWidget(self.signup_screen)
        self.addWidget(self.forgot_screen)
        self.addWidget(self.load_screen)
        self.addWidget(self.app_screen)

        self.setCurrentWidget(self.login_screen)


    def go_to_named_screen(self, screen_name, **kwargs):
        if screen_name == 'login':
            self.login_screen.set_username(kwargs['username'])
            self.login_screen.initiation_protocol()
            self.setCurrentWidget(self.login_screen)
            self.login_screen.update_lamby()
        elif(screen_name == 'signup'):
            self.setCurrentWidget(self.signup_screen)
            self.signup_screen.update_lamby()
        elif(screen_name == 'forgot'):
            self.forgot_screen.create_and_send_otp(kwargs['username'])
            self.setCurrentWidget(self.forgot_screen)
            self.forgot_screen.update_lamby()
        elif(screen_name == 'load'):
            self.load_screen.set_username(kwargs['username'])
            self.load_screen.initiation_protocol()
            self.setCurrentWidget(self.load_screen)
            self.load_screen.update_lamby()
        elif(screen_name == 'app'):
            self.app_screen.set_information(kwargs['username'], lesson_num=kwargs['lesson_num'], lesson_description=kwargs['lesson'], mode=kwargs['mode'])
            self.setCurrentWidget(self.app_screen)
        else:
            self.setCurrentWidget(self.login_screen)




