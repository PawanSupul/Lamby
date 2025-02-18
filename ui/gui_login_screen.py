import datetime

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QFrame, QLabel, QLineEdit, QCheckBox, QPushButton
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtCore import Qt, QSize
from user.credential import verify_user, get_all_registered_users, update_current_user, get_current_user, get_password_for_user
from ui.styles_login_screen import *
from functools import partial
from user.credential import save_credentials_when_signup

class LoginScreen(QWidget):
    def __init__(self, go_to_named_screen):
        super().__init__()
        self.go_to_named_screen = go_to_named_screen
        self.make_login_screen()
        self.initiation_protocol()



    def make_login_screen(self):
        self.login_layout = QVBoxLayout()

        self.username_layout = QHBoxLayout()
        self.username_label = QLabel("Username: ")
        self.username_label.setStyleSheet(label_style)
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet(input_style)
        self.username_layout.addWidget(self.username_label)
        self.username_layout.addWidget(self.username_input)
        self.username_error_label = QLabel("error")
        self.username_error_label.setStyleSheet(error_label_style)
        self.username_error_label.setFixedHeight(15)
        self.username_error_label.hide()

        self.password_layout = QHBoxLayout()
        self.password_label = QLabel("Password: ")
        self.password_label.setStyleSheet(label_style)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)     # Hide password
        self.password_input.setStyleSheet(input_style)
        self.password_view = QPushButton()
        self.password_view.setIcon(QIcon('images/unhide.png'))
        self.password_view.setFixedSize(35, 35)
        self.password_view.setStyleSheet(password_view_button_style)
        self.password_view.setIconSize(self.password_view.size() - QSize(10, 10))
        self.password_layout.addWidget(self.password_label)
        self.password_layout.addWidget(self.password_input)
        self.password_layout.addWidget(self.password_view)

        self.password_error_label = QLabel("error")
        self.password_error_label.setStyleSheet(error_label_style)
        self.password_error_label.setFixedHeight(15)
        self.password_error_label.hide()

        self.remember_me_checkbox = QCheckBox('Remember Me')
        self.remember_me_checkbox.setChecked(True)
        self.remember_me_checkbox.stateChanged.connect(self.handle_remember_me)
        self.remember_me_checkbox.setStyleSheet('background-color: #8cb7a4; font-size: 14px;')

        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet(login_button_style)

        self.signup_layout = QHBoxLayout()
        self.forgot_password_button = QPushButton("Forgot Password")
        self.forgot_password_button.setStyleSheet(borderless_button_style)
        self.sign_up_button = QPushButton("Sign Up")
        self.sign_up_button.setStyleSheet(borderless_button_style)
        self.signup_layout.addWidget(self.forgot_password_button)
        self.signup_layout.addWidget(self.sign_up_button)

        self.username_password_layout = QVBoxLayout()
        self.username_error_layout = QVBoxLayout()
        self.username_error_layout.addLayout(self.username_layout)
        self.username_error_layout.addWidget(self.username_error_label, alignment=Qt.AlignHCenter)
        self.password_error_layout = QVBoxLayout()
        self.password_error_layout.addLayout(self.password_layout)
        self.password_error_layout.addWidget(self.password_error_label, alignment=Qt.AlignHCenter)
        self.username_password_layout.addLayout(self.username_error_layout)
        self.username_password_layout.addLayout(self.password_error_layout)
        self.username_password_layout.addWidget(self.remember_me_checkbox, alignment=Qt.AlignHCenter)

        self.username_password_frame = QFrame()
        self.username_password_frame.setLayout(self.username_password_layout)
        self.username_password_frame.setStyleSheet("QFrame { border: 1px solid #5E81AC; }")

        self.login_layout.addWidget(self.username_password_frame)
        self.login_layout.addWidget(self.login_button)
        self.login_layout.addLayout(self.signup_layout)
        self.login_layout.setSpacing(20)

        self.login_container = QFrame()
        self.login_container.setLayout(self.login_layout)
        self.login_container.setFixedSize(550, 450)
        self.login_container.setStyleSheet(login_container_style)


        # self.central_widget.setLayout(self.login_layout)
        self.main_login_layout = QVBoxLayout()
        self.main_login_layout.addWidget(self.login_container, alignment=Qt.AlignCenter)

        self.setLayout(self.main_login_layout)

        self.password_view.clicked.connect(self.toggle_view_password)
        self.login_button.clicked.connect(self.handle_login)
        self.forgot_password_button.clicked.connect(self.handle_forgot_password)
        self.sign_up_button.clicked.connect(self.handle_sign_up)
        self.username_input.editingFinished.connect(self.validate_username)


    def handle_login(self):
        self.registered_user_list = get_all_registered_users()
        self.username = self.username_input.text()
        self.password = self.password_input.text()
        print(f'{self.username} - {self.password}')
        if(self.username == ''):
            self.set_username_error('Username empty!')
        elif(self.password == ''):
            self.set_password_error('Password empty!')
        elif(self.username not in self.registered_user_list):
            self.set_username_error('Username is not registered')
        else:
            verification_code = verify_user(self.username, self.password)
            if(verification_code == 0):
                self.load_user_account()
            elif(verification_code == 1):
                self.set_username_error('Username does not match any existing account')
            elif(verification_code == 2):
                self.set_password_error('Password is incorrect')
            elif(verification_code == 3):
                self.set_password_error('Password is corrupted! Please contact the administrator')
            elif(verification_code == 4):
                self.set_password_error('Password expired! Please update the password')
                self.update_password()
            else:
                print('error')

    def validate_username(self):
        username = self.username_input.text()
        if (username == ''):
            self.set_username_error('Username empty!')
            self.username_validated = False
        elif(username not in self.registered_user_list):
            self.set_username_error('Username is not registered')
            self.username_validated = False
        else:
            self.username_error_label.hide()
            self.username_validated = True

    def toggle_view_password(self):
        if (self.pw_show == False):
            self.pw_show = True
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.password_view.setIcon(QIcon('images/hide.png'))
        else:
            self.pw_show = False
            self.password_input.setEchoMode(QLineEdit.Password)
            self.password_view.setIcon(QIcon('images/unhide.png'))

    def set_username_error(self, text):
        self.username_error_label.setText(text)
        self.username_error_label.show()

    def set_password_error(self, text):
        self.password_error_label.setText(text)
        self.password_error_label.show()


    def handle_forgot_password(self):
        self.go_to_named_screen('signup')

    def handle_sign_up(self):
        self.go_to_named_screen('signup')


    def handle_remember_me(self, state):
        pass


    def update_password(self):
        pass


    def load_user_account(self):
        if(self.remember_me_checkbox.isChecked()):
            update_current_user(self.username)
        else:
            update_current_user('None')
        self.username_input.setText('')
        self.password_input.setText('')
        self.username_error_label.hide()
        self.password_error_label.hide()
        self.go_to_named_screen('load', username=self.username)


    def update_inputs_on_form(self):
        if self.current_user == 'None':
            username = ''
            password = ''
        else:
            username = self.current_user
            password = get_password_for_user(username)
        self.username_input.setText(username)
        self.password_input.setText(password)

    def set_username(self, username):
        self.current_user = username

    def initiation_protocol(self):
        self.username_error_label.hide()
        self.password_error_label.hide()
        self.registered_user_list = get_all_registered_users()
        self.current_user = get_current_user()
        self.update_inputs_on_form()
        self.username_validated = False
        self.pw_show = False
