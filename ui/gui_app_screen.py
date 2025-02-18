from PyQt5.QtWidgets import (QApplication, QStackedWidget, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
                             QWidget, QSizePolicy, QScrollArea, QLineEdit, QGraphicsOpacityEffect,
                             QButtonGroup, QCheckBox, QFrame, QMenu)
from PyQt5.QtGui import QPixmap, QScreen, QMouseEvent, QGuiApplication, QImage, QFontMetrics, QFont, QIcon, QColor
from PyQt5.QtCore import (Qt, QRect, QSize, QTimer, QPropertyAnimation, QEasingCurve, QAbstractAnimation,
                          QThread, pyqtSignal, QPoint)

from functools import partial
import asyncio
from googletrans import Translator
from ui.styles_app_screen import *
from engine.conversation_engine import ConversationEngine
from user.progress import add_completed_lesson_to_user
from user.credential import get_gender_for_user
from converter.speech_to_text import SpeachToText
from converter.text_to_speech import TextToSpeech_Microsoft


class AppScreen(QWidget):
    user_message_signal = pyqtSignal(str)
    reset_chat_signal = pyqtSignal()

    def __init__(self, go_to_named_screen):
        super().__init__()
        self.go_to_named_screen = go_to_named_screen
        self.translator = Translator()
        self.tranlator_loop = asyncio.get_event_loop()
        self.conversation_engine = ConversationEngine()
        self.worker_thread = QThread()
        self.conversation_engine.moveToThread(self.worker_thread)
        self.worker_thread.start()
        self.speech_to_text = SpeachToText()
        self.text_to_speech = TextToSpeech_Microsoft()

        self.username = ''
        self.previous_translation_src = ''
        self.previous_translation_dest = ''
        self.dialog_threshold_for_lesson_complete = 5
        self.clicked_button_id = None

    def set_information(self, username, **kwargs):
        self.username = username
        self.lesson_num = kwargs['lesson_num']
        self.lesson_description = kwargs['lesson_description']
        print(f'lesson: {self.lesson_description}')
        self.mode = kwargs['mode']
        self.conversation_engine.set_lesson_topic(self.lesson_description)
        gender = get_gender_for_user(self.username).lower()
        if (gender == 'male'):
            self.select_user.setIcon(QIcon('images/user_male.png'))
        elif (gender == 'female'):
            self.select_user.setIcon(QIcon('images/user_female.png'))
        else:
            self.select_user.setIcon(QIcon('images/user_other.png'))


    def make_app_screen(self):
        # Main Layout
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        # menu area
        self.menu_layout = QHBoxLayout()
        self.menu_layout.setContentsMargins(10, 0, 10, 0)

        self.reset_button = QPushButton()
        self.reset_button.setIcon(QIcon('images/refresh.png'))
        self.reset_button.setFixedSize(50, 40)
        self.reset_button.setIconSize(self.reset_button.size() - QSize(10, 10))
        self.reset_button.setStyleSheet(reset_style)

        self.clear_button = QPushButton()
        self.clear_button.setIcon(QIcon('images/dustbin.png'))
        self.clear_button.setFixedSize(50, 40)
        self.clear_button.setIconSize(self.clear_button.size() - QSize(10, 10))
        self.clear_button.setStyleSheet(clear_style)

        self.select_button_layout = QHBoxLayout()
        self.select_button_group = QButtonGroup()
        self.select_button_group.setExclusive(True)
        self.select_vocal = QPushButton()
        self.select_vocal.setFixedSize(80, 40)
        self.select_vocal.setIcon(QIcon('images/mic_4.png'))
        self.select_vocal.setIconSize(self.select_vocal.size() - QSize(10, 10))
        self.select_vocal.setStyleSheet(select_vocal_style)
        self.select_vocal.setCheckable(True)
        # self.select_vocal.setChecked(True)
        self.select_text = QPushButton()
        self.select_text.setFixedSize(80, 40)
        self.select_text.setIcon(QIcon('images/text.png'))
        self.select_text.setIconSize(self.select_text.size() - QSize(10, 10))
        self.select_text.setStyleSheet(select_text_style)
        self.select_text.setCheckable(True)
        self.select_text.setChecked(True)
        self.select_button_group.addButton(self.select_vocal, 1)
        self.select_button_group.addButton(self.select_text, 1)
        self.select_button_layout.addWidget(self.select_vocal)
        self.select_button_layout.addWidget(self.select_text)
        self.select_button_layout.setSpacing(5)

        self.select_back = QPushButton()
        self.select_back.setFixedSize(40, 40)
        self.select_back.setIcon(QIcon('images/back.png'))
        self.select_back.setIconSize(self.select_back.size() - QSize(10, 10))
        self.select_back.setStyleSheet(select_back_style)

        self.select_user = QPushButton()
        self.select_user.setFixedSize(40, 40)
        self.select_user.setIcon(QIcon('images/user_male.png'))
        self.select_user.setIconSize(self.select_user.size())
        self.select_user.setStyleSheet(select_user_style)
        self.user_menu = QMenu()
        self.user_menu.addAction('Logout', self.handle_logout)
        # self.select_user.setMenu(self.user_menu)

        self.menu_layout.addWidget(self.reset_button)
        self.menu_layout.addWidget(self.clear_button)
        self.menu_layout.addStretch()
        self.menu_layout.addWidget(self.select_back)
        self.menu_layout.addLayout(self.select_button_layout)
        self.menu_layout.addWidget(self.select_user)
        self.menu_layout.setSpacing(25)
        self.menu_container = QWidget()
        self.menu_container.setStyleSheet(menu_style)  #
        self.menu_container.setFixedHeight(50)
        self.menu_container.setLayout(self.menu_layout)

        self.translated_result = QLabel('This is the translated result')
        self.translated_result.setFont(QFont('Helvetica', 15))
        self.translated_result.setStyleSheet(translated_message_style)
        self.translated_result.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.translated_result.hide()

        # Scrollable chat area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_content.setStyleSheet("background-color: #e2d9d2; border:none")
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_area.setWidget(self.scroll_content)
        self.scroll_area.setStyleSheet(scrollbar_style)

        # Input field and send button
        self.input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setFont(QFont('Helvetica', 15))
        self.input_field.setStyleSheet(input_field_style)

        self.send_button_en = QPushButton("EN")
        # self.send_button_en.setIcon(QIcon('images/mic_3.png'))
        self.send_button_en.setFixedSize(60, 60)
        # self.send_button_en.setIconSize(self.send_button_en.size())
        self.send_button_en.setStyleSheet(button_en_style)
        self.send_button_en.setShortcut("e")

        self.send_button_es = QPushButton("ES")
        # self.send_button_es.setIcon(QIcon('images/mic_3.png'))
        self.send_button_es.setFixedSize(60, 60)
        # self.send_button_es.setIconSize(self.send_button_es.size())
        self.send_button_es.setStyleSheet(button_es_style)
        self.send_button_es.setShortcut("s")

        self.send_text_button = QPushButton()
        self.send_text_button.setIcon(QIcon('images/send.png'))
        self.send_text_button.setFixedSize(100, 60)
        self.send_text_button.setIconSize(self.send_text_button.size() - QSize(20, 20))
        self.send_text_button.setStyleSheet(send_text_button_style)
        self.send_text_button.setShortcut("Return")

        button_en_op = QGraphicsOpacityEffect(self)
        button_en_op.setOpacity(1.0)
        self.send_button_en.setGraphicsEffect(button_en_op)
        button_es_op = QGraphicsOpacityEffect(self)
        button_es_op.setOpacity(1.0)
        self.send_button_es.setGraphicsEffect(button_es_op)

        self.input_button_set_layout = QHBoxLayout()
        self.input_button_set_layout.addWidget(self.send_button_en)
        self.input_button_set_layout.addWidget(self.send_button_es)
        self.input_button_set_layout.addWidget(self.send_text_button)
        self.send_button_es.hide()
        self.send_button_en.hide()

        self.input_layout.addWidget(self.input_field)
        self.input_layout.addLayout(self.input_button_set_layout)
        self.input_container = QWidget()
        self.input_container.setLayout(self.input_layout)

        # Add widget to main layout
        self.main_layout.addWidget(self.menu_container)
        self.main_layout.addWidget(self.translated_result)
        self.main_layout.addWidget(self.scroll_area)
        self.main_layout.addWidget(self.input_container)

        self.setLayout(self.main_layout)

        # Button click events
        self.clear_button.clicked.connect(self.handle_clear)
        self.reset_button.clicked.connect(self.handle_reset)
        self.select_vocal.clicked.connect(self.handle_vocal_select)
        self.select_text.clicked.connect(self.handle_text_select)
        self.select_back.clicked.connect(self.handle_go_back)
        self.select_user.clicked.connect(self.show_user_menu)
        self.send_text_button.clicked.connect(self.send_message)
        self.send_button_en.clicked.connect(partial(self.animate_button, self.send_button_en, self.send_button_es))
        self.send_button_es.clicked.connect(partial(self.animate_button, self.send_button_es, self.send_button_en))

        self.user_message_signal.connect(self.conversation_engine.get_conversation_reply, Qt.QueuedConnection)
        self.reset_chat_signal.connect(self.conversation_engine.reset_conversation, Qt.QueuedConnection)
        self.conversation_engine.response_ready.connect(self.display_reply_from_system)
        self.conversation_engine.reset_success.connect(self.successful_reset)


    def show_user_menu(self):
        self.user_menu.exec_(self.select_user.mapToGlobal(QPoint(-60, self.select_user.height() + 5)))

    def send_message(self):
        text = self.input_field.text().strip()
        if text:
            self.add_message(text, "user")
            self.input_field.clear()
            # self.display_reply_from_system(text)
            self.user_message_signal.emit(text)

    def translate_process(self, es_text):
        if self.previous_translation_src == es_text:
            if self.translated_result.isVisible():
                self.translated_result.hide()
            else:
                self.translated_result.show()
        else:
            translated = self.tranlator_loop.run_until_complete(self.translate_from_spanish(es_text))
            self.previous_translation_src = es_text
            self.translated_result.setText(translated)
            self.translated_result.show()

        max_width = int(self.scroll_area.viewport().width() * 0.75)
        text_width = QFontMetrics(self.translated_result.font()).boundingRect(self.translated_result.text()).width() + 40
        if text_width > max_width:
            self.translated_result.setWordWrap(True)
            self.translated_result.setMaximumWidth(max_width)
        else:
            self.translated_result.setWordWrap(False)
            self.translated_result.setMaximumWidth((text_width))

    async def translate_from_spanish(self, es_text):
        translated = await self.translator.translate(es_text)
        return translated.text

    def display_reply_from_system(self, system_reply):
        reply_status = system_reply['status']
        reply_text = system_reply['text']
        # reply_text = """
        # text 1 \n text 2 \n text 3 \n text 4 \n text 5
        # """
        self.add_message(reply_text, "system")
        if(self.mode == 'story' and self.conversation_engine.num_dialogs > self.dialog_threshold_for_lesson_complete):
            add_completed_lesson_to_user(self.username, self.lesson_num)


    def add_message(self, text, sender):
        message_label = QLabel(text)
        font = QFont('Helvetica', 15)
        message_label.setFont(font)

        max_width = int(self.scroll_area.viewport().width() * 0.95)
        text_width = QFontMetrics(message_label.font()).boundingRect(message_label.text()).width() + 40

        if text_width > max_width:
            message_label.setWordWrap(True)
            message_label.setMaximumWidth(max_width)
        else:
            message_label.setWordWrap(False)
            message_label.setMaximumWidth((text_width))

        translate_button = QPushButton()
        translate_button.setIcon(QIcon('images/translate.png'))
        translate_button.setFixedSize(40, 40)
        translate_button.setIconSize(translate_button.size() - QSize(20, 20))
        translate_button.setStyleSheet(style_translate_button)
        translate_button.clicked.connect(partial(self.translate_process, text))

        message_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        message_layout = QHBoxLayout()
        if sender == "user":
            message_label.setStyleSheet(user_message_style)
            message_layout.addStretch(1)
            message_layout.addWidget(translate_button)
            message_layout.addWidget(message_label, 3)
        else:
            message_label.setStyleSheet(system_message_style)
            message_layout.addWidget(message_label, 3)
            message_layout.addWidget(translate_button)
            message_layout.addStretch(1)

        message_container = QWidget()
        message_container.setLayout(message_layout)
        self.scroll_layout.addWidget(message_container)
        QTimer.singleShot(0, self.update_message_widths)


    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_message_widths()


    def update_message_widths(self):
        max_width = int(self.scroll_area.viewport().width() * 0.75)

        for i in range(self.scroll_layout.count()):
            widget = self.scroll_layout.itemAt(i).widget()
            if widget:
                label = widget.findChild(QLabel)
                if label:
                    text_width = QFontMetrics(label.font()).boundingRect(label.text()).width() + 40

                    if text_width > max_width:
                        label.setWordWrap(True)
                        label.setMaximumWidth(max_width)
                    else:
                        label.setWordWrap(False)
                        label.setMaximumWidth(text_width)

        QTimer.singleShot(0, lambda: self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum()))


    def animate_button(self, clicked_button, other_button):
        # self.send_message()
        """Animate button expansion and shrinkage when clicked"""
        if self.clicked_button_id == None:
            shutit = False
        elif(clicked_button != self.clicked_button_id):
            shutit = False
        else:
            shutit = True
        self.clicked_button_id = clicked_button

        low_opacity = 0.5
        high_opacity = 1.0

        self.opacity_anim = QPropertyAnimation(clicked_button.graphicsEffect(), b"opacity")
        self.opacity_anim.setDuration(1000)
        self.opacity_anim.setStartValue(high_opacity)
        self.opacity_anim.setKeyValueAt(0.5, low_opacity)
        self.opacity_anim.setEndValue(high_opacity)
        self.opacity_anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.opacity_anim.setLoopCount(-1)  # Infinite loop

        self.opacity_anim.start()

        if hasattr(other_button, "opacity_animation"):
            other_button.opacity_animation.stop()
            other_button.graphicsEffect().setOpacity(1.0)
        clicked_button.opacity_animation = self.opacity_anim

        if shutit == True:
            clicked_button.opacity_animation.stop()
            self.clicked_button_id = None

        if clicked_button == self.send_button_es:
            print('pressed button is ES')
            self.speech_to_text.set_model("es")
            speech = self.speech_to_text.speech_to_text_dynamic()
            self.input_field.setText(speech)
        else:
            print('pressed button is EN')
            self.speech_to_text.set_model("en")
            speech = self.speech_to_text.speech_to_text_dynamic()
            self.input_field.setText(speech)
        self.send_message()

    def handle_clear(self):
        print('clear button pressed')
        for i in range(self.scroll_layout.count()):
            widget = self.scroll_layout.itemAt(i).widget()
            print(widget)
            widget.deleteLater()


    def handle_reset(self):
        print('reset button pressed')
        self.handle_clear()
        print("""clear chatgpt memory and start anew""")
        self.reset_chat_signal.emit()

    def successful_reset(self, response):
        if(response == 'successful'):
            print('Acknowledge from engine')

    def handle_vocal_select(self):
        self.send_button_en.show()
        self.send_button_es.show()
        self.send_text_button.hide()


    def handle_text_select(self):
        self.send_button_en.hide()
        self.send_button_es.hide()
        self.send_text_button.show()


    def handle_go_back(self):
        print('Go back')
        self.handle_reset()
        self.go_to_named_screen('load', username=self.username)

    def handle_logout(self):
        print('log out')
        self.handle_reset()
        self.go_to_named_screen('login', username=self.username)


    def closeEvent(self, event):
        self.worker_thread.quit()
        self.worker_thread.wait()
        event.accept()

# if __name__ == '__main__':
#     app = AppScreen()
#     app.translate_process('te amo julia')