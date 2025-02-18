from PyQt5.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QSizePolicy,
    QLineEdit, QComboBox, QPushButton, QMessageBox, QMainWindow, QWidget, QFrame, QGroupBox, QMenu
)
from PyQt5.QtCore import Qt, QSize, QPoint
from PyQt5.QtGui import QPainter, QPen, QIcon
import pandas as pd
import numpy as np
import random
from user.progress import get_completed_lessons
from user.credential import get_gender_for_user
from ui.styles_app_screen import select_back_style, select_user_style, menu_style
from ui.styles_load_screen import (scroll_content_style, section_button_style, section_lesson_container_style,
                                   lesson_button_style, scrollbar_style, quick_chat_button_style,
                                   storyline_container_style, hide_lesson_button_style,
                                   update_section_buttons_styles, update_lesson_buttons_styles)
from functools import partial

class LoadScreen(QWidget):
    def __init__(self, go_to_named_screen):
        super().__init__()
        self.go_to_named_screen = go_to_named_screen
        self.story_df = pd.read_excel('data/story_data/story.xlsx')
        self.num_lesson_columns = 3
        self.make_loading_screen()


    def set_username(self, username):
        self.username = username


    def make_loading_screen(self):
        print('make load screen')
        self.load_layout = QVBoxLayout()
        self.load_layout.setContentsMargins(0, 0, 0, 0)
        self.load_layout.setSpacing(0)

        self.menu_layout = QHBoxLayout()
        self.menu_layout.setContentsMargins(10, 0, 10, 0)
        self.menu_layout.setSpacing(25)

        self.select_back = QPushButton()
        self.select_back.setFixedSize(40, 40)
        self.select_back.setIcon(QIcon('images/back.png'))
        self.select_back.setIconSize(self.select_back.size() - QSize(10, 10))
        self.select_back.setStyleSheet(select_back_style)
        self.select_back.clicked.connect(self.handle_go_back)

        self.select_user = QPushButton()
        self.select_user.setFixedSize(40, 40)
        self.select_user.setIcon(QIcon('images/user_male.png'))
        self.select_user.setIconSize(self.select_user.size())
        self.select_user.setStyleSheet(select_user_style)
        self.user_menu = QMenu()
        self.user_menu.addAction('Logout', self.handle_logout)
        self.select_user.clicked.connect(self.show_user_menu)

        self.menu_layout.addStretch()
        self.menu_layout.addWidget(self.select_back)
        self.menu_layout.addWidget(self.select_user)

        self.menu_container = QWidget()
        self.menu_container.setStyleSheet(menu_style)  #
        self.menu_container.setFixedHeight(50)
        self.menu_container.setLayout(self.menu_layout)

        self.quick_start_layout = QHBoxLayout()

        self.quick_simple_chat_button = QPushButton('Quick Simple Chat')
        self.quick_simple_chat_button.setStyleSheet(quick_chat_button_style)
        self.quick_simple_chat_button.clicked.connect(self.handle_simple_chat)
        self.quick_random_chat_button = QPushButton('Quick Random Chat')
        self.quick_random_chat_button.setStyleSheet(quick_chat_button_style)
        self.quick_random_chat_button.clicked.connect(self.handle_random_chat)
        self.quick_start_layout.addWidget(self.quick_simple_chat_button)
        self.quick_start_layout.addWidget(self.quick_random_chat_button)
        self.quick_start_layout.setSpacing(20)

        self.storyline_layout = QVBoxLayout()
        self.section_layout = QHBoxLayout()
        self.section_layout.setContentsMargins(00, 10, 0, 10)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_content = QWidget()
        self.scroll_content.setStyleSheet(scroll_content_style)
        self.scroll_layout = QVBoxLayout()
        self.scroll_layout.setAlignment(Qt.AlignTop)
        # self.scroll_layout.setContentsMargins(0, 0, 0, 0)

        # Set layout for the scrollable content
        self.scroll_content.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_content)
        self.scroll_area.setStyleSheet(scrollbar_style)

        self.add_section_and_lesson_bubbles()

        self.storyline_layout.addLayout(self.section_layout)
        self.storyline_layout.addWidget(self.scroll_area)
        # self.storyline_layout.setContentsMargins(20,20,20,20)
        # self.storyline_layout.setSpacing(20)

        self.storyline_container = QFrame()
        self.storyline_container.setStyleSheet(storyline_container_style)
        self.storyline_container.setLayout(self.storyline_layout)
        # self.storyline_container.layout().setContentsMargins(20,20,20,20)

        self.main_load_layout = QVBoxLayout()
        self.main_load_layout.addLayout(self.quick_start_layout)
        story_line_label = QLabel('Story Line')
        story_line_label.setStyleSheet('font-size: 16px; font-weight:bold; color: black; padding-top: 20px; padding-left:10px;')
        self.main_load_layout.addWidget(story_line_label)
        self.main_load_layout.addWidget(self.storyline_container)
        self.main_load_layout.setContentsMargins(10, 15, 10, 15)
        self.main_load_layout.setSpacing(10)

        self.load_layout.addWidget(self.menu_container)
        self.load_layout.addLayout(self.main_load_layout)

        self.setLayout(self.load_layout)


    def add_section_and_lesson_bubbles(self):
        num_sections = self.story_df.loc[:, 'section'].unique().tolist()
        for idx, section in enumerate(num_sections):
            button = QPushButton(f'S {section}')
            button.setFixedSize(100, 100)
            button.setStyleSheet(section_button_style)
            self.section_layout.addWidget(button)
            button.clicked.connect(partial(self.handle_section_buttons, section))
            setattr(self, f'section_button_{section}', button)

            lesson_container = QVBoxLayout()
            lesson_container.setContentsMargins(10, 0, 10, 0)
            section_lesson_container = QWidget()
            section_lesson_container.setLayout(lesson_container)
            section_lesson_container.setStyleSheet(section_lesson_container_style)
            self.scroll_layout.addWidget(section_lesson_container)

            setattr(self, f'lesson_container_{section}', lesson_container)
            setattr(self, f'lesson_container_section_{section}', section_lesson_container)

            lesson_df = self.get_lessons_of_section(section)
            total_lessons = lesson_df.shape[0]

            rows = total_lessons//self.num_lesson_columns
            index = 0
            for r in range(rows):
                setattr(self, f'lesson_row_{r}_layout', QHBoxLayout())
                for c in range(self.num_lesson_columns):
                    local_lesson_number = int(lesson_df.loc[index, 'sub lesson'])
                    global_lesson_number = int(lesson_df.loc[index, 'lesson'])
                    lesson_description = lesson_df.loc[index, 'description']

                    button_text = f'({local_lesson_number}/{total_lessons}) - {global_lesson_number} - {lesson_description}'
                    button = QPushButton(button_text)
                    button.setStyleSheet(lesson_button_style)
                    getattr(self, f'lesson_row_{r}_layout').addWidget(button)
                    button.clicked.connect(partial(self.handle_lesson_buttons, global_lesson_number))
                    setattr(self, f'lesson_button_{global_lesson_number}', button)
                    index += 1
                lesson_container.addLayout(getattr(self, f'lesson_row_{r}_layout'))
            setattr(self, f'lesson_row_{r+1}_layout', QHBoxLayout())
            # remaining = total_lessons - (index)
            if total_lessons%self.num_lesson_columns != 0:
                for c in range(3):
                    if index < total_lessons:
                        local_lesson_number = int(lesson_df.loc[index, 'sub lesson'])
                        global_lesson_number = int(lesson_df.loc[index, 'lesson'])
                        lesson_description = lesson_df.loc[index, 'description']
                        button_text = f'({local_lesson_number}/{total_lessons}) - {global_lesson_number} - {lesson_description}'
                        button = QPushButton(button_text)
                        button.setStyleSheet(lesson_button_style)
                        getattr(self, f'lesson_row_{r+1}_layout').addWidget(button)
                        button.clicked.connect(partial(self.handle_lesson_buttons, global_lesson_number))
                        setattr(self, f'lesson_button_{global_lesson_number}', button)
                        index += 1
                    else:
                        button = QPushButton('')
                        button.setStyleSheet(hide_lesson_button_style)
                        getattr(self, f'lesson_row_{r + 1}_layout').addWidget(button)
                        index += 1
            lesson_container.addLayout(getattr(self, f'lesson_row_{r+1}_layout'))

            getattr(self, f'lesson_container_section_{section}').hide()


    def handle_simple_chat(self):
        lesson_description = 'general conversation'
        self.go_to_named_screen('app', username=self.username, lesson=lesson_description, lesson_num=None, mode='simple')


    def handle_random_chat(self):
        completed_lessons = get_completed_lessons(self.username)
        random_lesson = random.choice(completed_lessons)
        lesson_description = self.story_df.loc[self.story_df.loc[:, 'lesson'] == random_lesson, 'description'].values[0]
        self.go_to_named_screen('app', username=self.username, lesson=lesson_description, lesson_num=None, mode='random')


    def handle_section_buttons(self, section_num):
        print(f'handle section {section_num}')

        list_sections = self.story_df.loc[:, 'section'].unique().tolist()
        hide_sections = [x for x in list_sections if x != section_num]
        for section in hide_sections:
            getattr(self, f'lesson_container_section_{section}').hide()       # setStyleSheet('color: red; border-radius: 10px;')
            # getattr(self, f'section_button_{section}').setStyleSheet('QPushButoon{ border: none; }')
        getattr(self, f'lesson_container_section_{section_num}').show()
        # getattr(self, f'section_button_{section_num}').setStyleSheet('QPushButoon{ border: 2px solid red; }')

        for section in list_sections:
            if(section in hide_sections):
                firstbit = '0'
            else:
                firstbit = '1'
            if(section in self.completed_sections):
                secondbit = '0'
            elif(section in self.ongoing_sections):
                secondbit = '1'
            else:
                secondbit = '2'
            mode = firstbit + secondbit
            update_section_buttons_styles(getattr(self, f'section_button_{section}'), mode)


    def handle_lesson_buttons(self, lesson_num):
        lesson_description = self.story_df.loc[self.story_df.loc[:, 'lesson'] == lesson_num, 'description'].values[0]
        self.go_to_named_screen('app', username=self.username, lesson=lesson_description, lesson_num=lesson_num, mode='story')

    def update_story_line_progress(self):
        for idx, section in enumerate(self.incomplete_sections):
            button = getattr(self, f'section_button_{section}')
            update_section_buttons_styles(button, '02')
        for idx, section in enumerate(self.ongoing_sections):
            button = getattr(self, f'section_button_{section}')
            update_section_buttons_styles(button, '01')
        for idx, section in enumerate(self.completed_sections):
            button = getattr(self, f'section_button_{section}')
            update_section_buttons_styles(button, '00')

        for idx, lesson in enumerate(self.incomplete_lessons):
            button = getattr(self, f'lesson_button_{lesson}')
            update_lesson_buttons_styles(button, 1)
        for idx, lesson in enumerate(self.completed_lessons):
            button = getattr(self, f'lesson_button_{lesson}')
            update_lesson_buttons_styles(button, 0)

    def get_lessons_of_section(self, section_num):
        lesson_df = self.story_df.loc[self.story_df.loc[:, 'section'] == section_num, ['lesson', 'sub lesson', 'description']]
        return lesson_df.reset_index()


    def get_complete_and_incomplete_sections(self, username):
        all_lessons = self.story_df.loc[:, 'lesson'].tolist()
        completed_lessons = get_completed_lessons(username)
        incomplete_lessons = [x for x in all_lessons if x not in completed_lessons]
        temp_incomplete_sections = self.story_df[self.story_df['lesson'].isin(incomplete_lessons)]['section'].unique()
        temp_complete_sections = self.story_df[self.story_df['lesson'].isin(completed_lessons)]['section'].unique()

        ongoing_sections = np.intersect1d(temp_complete_sections, temp_incomplete_sections)
        completed_sections = np.setdiff1d(temp_complete_sections, temp_incomplete_sections)
        incomplete_sections = np.setdiff1d(temp_incomplete_sections, temp_complete_sections)

        return completed_sections, ongoing_sections, incomplete_sections, completed_lessons, incomplete_lessons

    def show_user_menu(self):
        self.user_menu.exec_(self.select_user.mapToGlobal(QPoint(-60, self.select_user.height() + 5)))

    def handle_go_back(self):
        print('Go back')
        self.go_to_named_screen('login', username=self.username)

    def handle_logout(self):
        print('log out')
        self.go_to_named_screen('login', username=self.username)

    def initiation_protocol(self):
        gender = get_gender_for_user(self.username).lower()
        if(gender == 'male'):
            self.select_user.setIcon(QIcon('images/user_male.png'))
        elif(gender == 'female'):
            self.select_user.setIcon(QIcon('images/user_female.png'))
        else:
            self.select_user.setIcon(QIcon('images/user_other.png'))
        (self.completed_sections, self.ongoing_sections, self.incomplete_sections,
         self.completed_lessons, self.incomplete_lessons) = self.get_complete_and_incomplete_sections(self.username)
        print(self.completed_lessons)
        print(self.completed_sections)
        print(self.incomplete_sections)
        self.update_story_line_progress()

