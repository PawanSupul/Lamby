from PyQt5.QtWidgets import (QVBoxLayout, QHBoxLayout, QWidget, QFrame, QLabel, QLineEdit, QPushButton,
                             QRadioButton, QButtonGroup)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize
from ui.styles_login_screen import *
from user.credential import save_credentials_when_signup, get_all_registered_users, get_current_user


class SignUpScreen(QWidget):
    def __init__(self, go_to_named_screen):
        super().__init__()
        self.go_to_named_screen = go_to_named_screen
        self.label_width = 130
        self.pw_1_show = False
        self.pw_2_show = False
        self.age_validated = False
        self.password_validated = False
        self.username_validate = False
        self.make_signup_page()

    def make_signup_page(self):
        self.signup_layout = QVBoxLayout()

        topic = QLabel("Sign-up for Lamby")
        topic.setAlignment(Qt.AlignCenter)
        topic.setMaximumHeight(80)
        topic.setStyleSheet("color: navy; font-size: 26px;")

        self.name_layout = QHBoxLayout()
        self.age_layout = QHBoxLayout()
        self.gender_layout = QHBoxLayout()
        self.username_layout = QHBoxLayout()
        self.password_1_layout = QHBoxLayout()
        self.password_2_layout = QHBoxLayout()
        self.button_layout = QHBoxLayout()

        name_label = QLabel("Your Name: ")
        name_label.setFixedWidth(self.label_width)
        name_label.setStyleSheet(signup_label_style)
        self.name_entry = QLineEdit()
        self.name_entry.setStyleSheet(signup_entry_style)
        self.name_layout.addWidget(name_label)
        self.name_layout.addWidget(self.name_entry)
        age_label = QLabel("Your Age: ")
        age_label.setFixedWidth(self.label_width)
        age_label.setStyleSheet(signup_label_style)
        self.age_entry = QLineEdit()
        self.age_entry.setStyleSheet(signup_entry_style)
        self.age_layout.addWidget(age_label)
        self.age_layout.addWidget(self.age_entry)

        gender_label = QLabel("Gender: ")
        gender_label.setFixedWidth(self.label_width)
        gender_label.setStyleSheet(signup_label_style)
        self.radio_male = QRadioButton("Male")
        self.radio_male.setStyleSheet(signup_radio_button_style)
        self.radio_female = QRadioButton("Female")
        self.radio_female.setStyleSheet(signup_radio_button_style)
        self.radio_other = QRadioButton("Other")
        self.radio_other.setStyleSheet(signup_radio_button_style)
        self.gender_button_group = QButtonGroup()
        self.gender_button_group.addButton(self.radio_male)
        self.gender_button_group.addButton(self.radio_female)
        self.gender_button_group.addButton(self.radio_other)
        self.gender_button_group.setExclusive(True)
        self.gender_layout.addWidget(gender_label)
        self.gender_layout.addWidget(self.radio_male)
        self.gender_layout.addWidget(self.radio_female)
        self.gender_layout.addWidget(self.radio_other)

        username_label = QLabel("Username: ")
        username_label.setFixedWidth(self.label_width)
        username_label.setStyleSheet(signup_label_style)
        self.username_entry = QLineEdit()
        self.username_entry.setStyleSheet(signup_entry_style)
        self.username_layout.addWidget(username_label)
        self.username_layout.addWidget(self.username_entry)
        password_1_label = QLabel("Enter Password: ")
        password_1_label.setFixedWidth(self.label_width)
        password_1_label.setStyleSheet(signup_label_style)
        self.password_1_entry = QLineEdit()
        self.password_1_entry.setEchoMode(QLineEdit.Password)
        self.password_1_entry.setStyleSheet(signup_entry_style)
        self.password_1_view = QPushButton()
        self.password_1_layout.addWidget(password_1_label)
        self.password_1_layout.addWidget(self.password_1_entry)
        self.password_1_layout.addWidget(self.password_1_view)
        password_2_label = QLabel("Re-enter Password: ")
        password_2_label.setFixedWidth(self.label_width)
        password_2_label.setStyleSheet(signup_label_style)
        self.password_2_entry = QLineEdit()
        self.password_2_entry.setEchoMode(QLineEdit.Password)
        self.password_2_entry.setStyleSheet(signup_entry_style)
        self.password_2_view = QPushButton()
        self.password_2_layout.addWidget(password_2_label)
        self.password_2_layout.addWidget(self.password_2_entry)
        self.password_2_layout.addWidget(self.password_2_view)

        self.password_1_view.setIcon(QIcon('images/unhide.png'))
        self.password_1_view.setFixedSize(35, 35)
        self.password_1_view.setStyleSheet(password_view_button_style)
        self.password_1_view.setIconSize(self.password_1_view.size()-QSize(10, 10))
        self.password_2_view.setIcon(QIcon('images/unhide.png'))
        self.password_2_view.setFixedSize(35, 35)
        self.password_2_view.setStyleSheet(password_view_button_style)
        self.password_2_view.setIconSize(self.password_2_view.size() - QSize(10, 10))

        self.signup_button = QPushButton('Sign Up')
        self.signup_button.setStyleSheet(signup_button_style)
        self.cancel_button = QPushButton('Cancel')
        self.cancel_button.setStyleSheet(signup_button_style)
        self.button_layout.addWidget(self.signup_button)
        self.button_layout.addWidget(self.cancel_button)

        self.error_age_label = QLabel('You must be 18 years or older to sign up!')
        self.error_age_label.setStyleSheet(error_label_style)
        self.error_age_label.setAlignment(Qt.AlignCenter)
        self.error_age_label.setMaximumHeight(20)
        self.error_age_label.hide()
        self.error_username_label = QLabel('Username already exists. Use a different username!')
        self.error_username_label.setStyleSheet(error_label_style)
        self.error_username_label.setAlignment(Qt.AlignCenter)
        self.error_username_label.setMaximumHeight(20)
        self.error_username_label.hide()
        self.error_password_label = QLabel('Passwords do NOT match!')
        self.error_password_label.setStyleSheet(error_label_style)
        self.error_password_label.setAlignment(Qt.AlignCenter)
        self.error_password_label.setMaximumHeight(20)
        self.error_password_label.hide()
        self.error_form_label = QLabel('Form error')
        self.error_form_label.setStyleSheet(error_label_style)
        self.error_form_label.setAlignment(Qt.AlignCenter)
        self.error_form_label.setMaximumHeight(20)
        self.error_form_label.hide()

        self.signup_layout.addWidget(topic, alignment=Qt.AlignHCenter)
        self.signup_layout.addLayout(self.name_layout)
        self.signup_layout.addLayout(self.age_layout)
        self.signup_layout.addWidget(self.error_age_label)
        self.signup_layout.addLayout(self.gender_layout)
        self.signup_layout.addLayout(self.username_layout)
        self.signup_layout.addWidget(self.error_username_label)
        self.signup_layout.addLayout(self.password_1_layout)
        self.signup_layout.addLayout(self.password_2_layout)
        self.signup_layout.addWidget(self.error_password_label)
        self.signup_layout.addLayout(self.button_layout)
        self.signup_layout.addWidget(self.error_form_label)

        self.signup_container = QFrame()
        self.signup_container.setLayout(self.signup_layout)
        self.signup_container.setFixedSize(550, 650)
        self.signup_container.setStyleSheet(login_container_style)

        self.main_signup_layout = QVBoxLayout()
        self.main_signup_layout.addWidget(self.signup_container, alignment=Qt.AlignCenter)

        self.setLayout(self.main_signup_layout)

        self.password_1_view.clicked.connect(self.toggle_view_password_1)
        self.password_2_view.clicked.connect(self.toggle_view_password_2)
        self.password_2_entry.textChanged.connect(self.validate_password)
        self.age_entry.editingFinished.connect(self.validate_age)
        self.username_entry.editingFinished.connect(self.validate_username)
        self.signup_button.clicked.connect(self.handle_signup)
        self.cancel_button.clicked.connect(self.handle_cancel)

    def toggle_view_password_1(self):
        if(self.pw_1_show == False):
            self.pw_1_show = True
            self.password_1_entry.setEchoMode(QLineEdit.Normal)
            self.password_1_view.setIcon(QIcon('images/hide.png'))
        else:
            self.pw_1_show = False
            self.password_1_entry.setEchoMode(QLineEdit.Password)
            self.password_1_view.setIcon(QIcon('images/unhide.png'))

    def toggle_view_password_2(self):
        if (self.pw_2_show == False):
            self.pw_2_show = True
            self.password_2_entry.setEchoMode(QLineEdit.Normal)
            self.password_2_view.setIcon(QIcon('images/hide.png'))
        else:
            self.pw_2_show = False
            self.password_2_entry.setEchoMode(QLineEdit.Password)
            self.password_2_view.setIcon(QIcon('images/unhide.png'))


    def validate_name(self):
        name = self.name_entry.text()
        if(len(name) > 2):
            self.error_form_label.hide()


    def validate_age(self):
        age_text = self.age_entry.text()
        if( age_text.isdigit() ):
            age = int(age_text)
            if( 18 <= age <= 100):
                self.error_age_label.hide()
                self.error_form_label.hide()
                self.age_validated = True
            elif(age < 18):
                self.error_age_label.setText('You must be 18 years or older to sign up!')
                self.error_age_label.show()
                self.age_validated = False
            else:
                self.error_age_label.setText('Enter a valid age!')
                self.error_age_label.show()
                self.age_validated = False
        else:
            self.error_age_label.setText('Enter a valid age as a number!')
            self.error_age_label.show()
            self.age_validated = False


    def validate_username(self):
        all_users = get_all_registered_users()
        username = self.username_entry.text()
        if (username not in all_users):
            self.username_validate = True
            self.error_username_label.hide()
        else:
            self.username_validate = False
            self.error_username_label.show()

    def validate_password(self):
        password_1 = self.password_1_entry.text()
        password_2 = self.password_2_entry.text()
        if(password_1 == password_2):
            self.error_password_label.hide()
            self.error_form_label.hide()
            self.password_validated = True
        else:
            self.error_password_label.setText('Passwords do NOT match!')
            self.error_password_label.show()
            self.password_validated = False

    def get_gender(self):
        if self.radio_male.isChecked():
            gender = 'Male'
        elif self.radio_female.isChecked():
            gender = 'Female'
        elif self.radio_other.isChecked():
            gender = 'Other'
        else:
            gender = 'Other'
        return gender

    def handle_signup(self):
        if (self.age_validated and self.password_validated and self.username_validate):
            name = self.name_entry.text()
            age = self.age_entry.text()
            gender = self.get_gender()
            username = self.username_entry.text()
            password = self.password_1_entry.text()
            if( len(name) > 2 ):
                self.error_form_label.hide()
                info_dict = {
                    "name": name,
                    "age": age,
                    "gender": gender,
                    "username": username,
                    "password": password
                }
                save_credentials_when_signup(info_dict)
                self.go_to_login_screen(username)
            else:
                self.error_form_label.setText('Complete the form correctly to continue!')
                self.error_form_label.show()
        else:
            self.error_form_label.setText('Complete the form correctly to continue!')
            self.error_form_label.show()


    def handle_cancel(self):
        self.name_entry.setText('')
        self.age_entry.setText('')
        for gb in self.gender_button_group.buttons():
            if gb.isChecked():
                gb.setChecked(False)
        self.username_entry.setText('')
        self.password_1_entry.setText('')
        self.password_2_entry.setText('')

        self.error_age_label.hide()
        self.error_password_label.hide()
        self.error_form_label.hide()

        self.go_to_named_screen('login', username=get_current_user())


    def go_to_login_screen(self, username):
        self.name_entry.setText('')
        self.age_entry.setText('')
        for gb in self.gender_button_group.buttons():
            if gb.isChecked():
                gb.setChecked(False)
        self.username_entry.setText('')
        self.password_1_entry.setText('')
        self.password_2_entry.setText('')

        self.error_age_label.hide()
        self.error_password_label.hide()
        self.error_form_label.hide()
        self.go_to_named_screen('login', username=username)

