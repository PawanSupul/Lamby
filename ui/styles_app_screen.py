color_reset_normal = '#8cb7a4'
color_reset_hover = '#999999'
color_reset_press = '#808080'

color_send_normal = '#8cb7a4'
color_send_hover = '#72a78f'
color_send_press = '#588d75'

color_voice_normal = '#b3b3b3'
color_voice_hover = '#999999'
color_voice_press = '#808080'
color_voice_latched = '#85aac6'


reset_style = """
    QPushButton {
            background-color: %s;
            border-radius: 20px;
            border: None;
        }
    QPushButton:hover {
            background-color: %s;
        }
    QPushButton:pressed {
            background-color: %s; 
            border: 1px solid black;
        }
    """%(color_reset_normal, color_reset_hover, color_reset_press)


clear_style = """
    QPushButton {
            background-color: %s;
            border-radius: 20px;
            border: None;
        }
    QPushButton:hover {
            background-color: %s;
        }
    QPushButton:pressed {
            background-color: %s;
            border: 1px solid black;
        }
"""%(color_reset_normal, color_reset_hover, color_reset_press)


select_back_style = clear_style


select_user_style = """
    QPushButton {
            border-radius: 20px;
            border: none;
        }
    QPushButton:hover {
            border: 1px solid black;
        }
    QPushButton:pressed {
            border: 2px solid black;
        }
"""


select_vocal_style = """
    QPushButton {
            background-color: %s;
            border-radius: 20px;
            border: None;
        }
    QPushButton:hover {
            background-color: %s;
        }
    QPushButton:checked {
            background-color: %s; 
            border: 1px solid black;
        }
"""%(color_reset_normal, color_reset_hover, color_reset_press)


select_text_style = """
    QPushButton {
            background-color: %s;
            border-radius: 20px;
            border: None;
        }
    QPushButton:hover {
            background-color: %s;
        }
    QPushButton:checked {
            background-color: %s;
            border: 1px solid black;
        }
"""%(color_reset_normal, color_reset_hover, color_reset_press)


menu_style = """
    background-color: #8cb7a4; border-radius: 0px; border:none;
"""


input_field_style = """
    border-radius: 25px; background-color: white; height: 3em; padding: 3px;
"""


button_en_style = """
    QPushButton {
            background-color: %s;
            border-radius: 30px;
            border: None;
            background-image: url(images/english_unselect.png);
            background-repeat: no-repeat;
            background-position: center;
        }
    QPushButton:hover {
            background-color: %s;
            background-image: url(images/english_select.png);
        }
    QPushButton:checked {
            background-color: %s; 
            background-image: url(images/english_select.png);
        }
"""%(color_voice_normal, color_voice_hover, color_voice_latched)


button_es_style = """
    QPushButton {
            background-color: %s;
            border-radius: 30px;
            border: None;
            background-image: url(images/spanish_unselect.png);
            background-repeat: no-repeat;
            background-position: center;
        }
    QPushButton:hover {
            background-color: %s;
            background-image: url(images/spanish_select.png);
        }
    QPushButton:checked {
            background-color: %s; 
            background-image: url(images/spanish_select.png);
        }
"""%(color_voice_normal, color_voice_hover, color_voice_latched)


send_text_button_style = """
    QPushButton {
            background-color: transparent;  /* #8cb7a4; */
            border-radius: 20px;
            border: None;
        }
    QPushButton:hover {
            background-color: %s; 
        }
    QPushButton:pressed {
            background-color: %s; 
            border: 2px solid black
        }
"""%(color_reset_hover, color_reset_press)


translated_message_style = """
    QLabel {
        background-color: #c0dbff; 
        color: red;
        padding: 8px; 
        letter-spacing: 0.1em;
        border-radius: 10px;
    }
"""


style_translate_button = """
    QPushButton {
            background-color: #e2d9d2;
            border-radius: 10px;
            border: None;
        }
    QPushButton:hover{
        background-color: #ccbbad;
    }
    QPushButton:checked {
            background-color: #b1957f;
        }
"""


user_message_style = """
    background-color: #e5fdcb; 
    padding: 8px; 
    margin: 5px; 
    letter-spacing: 0.1em;
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
    border-bottom-left-radius: 15px;
"""


system_message_style = """
    background-color: white; 
    padding: 8px; 
    margin: 5px; 
    letter-spacing: 0.1em;
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
    border-bottom-right-radius: 15px;
"""


scrollbar_style = """
    QScrollArea {
        border: 2px solid transparent;
        border-radius: 5px;
    }
    
    QScrollBar:vertical {
        border: none;
        background: #d7cfc7; 
        width: 12px;
        margin: 0px 0px 0px 0px;
        border-radius: 6px; 
    }

    QScrollBar::handle:vertical {
         background: qlineargradient(                 
             x1:0, y1:0, x2:1, y2:1,                   
             stop:0 #83b6a0, stop:1 #74a28e           
         );                                           
        border: none;
        min-height: 20px;
        border-radius: 6px;  
    }

    QScrollBar::handle:vertical:hover {
         background: qlineargradient(             
             x1:0, y1:0, x2:1, y2:1,              
             stop:0 #8bc1a9, stop:1 #7eb09a      
         );     
    }
    
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        border: none;
        background: none;
        height: 0px;
    }

    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
        border: none;
        background: none;
    }
"""

