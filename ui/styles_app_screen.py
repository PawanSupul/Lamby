reset_style = """
    QPushButton {
            background-color: #baa488;
            border-radius: 20px;
            border: None;
        }
    QPushButton:pressed {
            background-color: #aa957a; /* Change background when pressed */
            border: 1px solid black;
        }
    """

clear_style = """
    QPushButton {
            background-color: #baa488;
            border-radius: 20px;
            border: None;
        }
    QPushButton:pressed {
            background-color: #aa957a; /* Change background when pressed */
            border: 1px solid black;
        }
"""


select_back_style = """
"""


select_user_style = """
"""


select_vocal_style = """
    QPushButton {
            background-color: #baa488;
            border-top-left-radius: 20px;
            border-bottom-left-radius: 20px;
            border: None;
        }
    QPushButton:checked {
            background-color: #aa957a; /* Change background when pressed */
            border: 1px solid black;
        }
"""

select_text_style = """
    QPushButton {
            background-color: #baa488;
            border-top-right-radius: 20px;
            border-bottom-right-radius: 20px;
            border: None;
        }
    QPushButton:checked {
            background-color: #aa957a; /* Change background when pressed */
            border: 1px solid black;
        }
"""

menu_style = """
    background-color: #8cb7a4; border-radius: 0px; border:none;
"""

input_field_style = """
    border-radius: 25px; background-color: white; height: 3em; padding: 3px;
"""

button_en_style = """
    border-radius: 30px; border: none; background-color: #8cb7a4
"""

button_es_style = """
    border-radius: 30px; border: none; background-color: #baa488
"""

send_text_button_style = """
    QPushButton {
            background-color: #8cb7a4;
            border-radius: 20px;
            border: None;
        }
    QPushButton:pressed {
            background-color: #6e8d7f; /* Change background when pressed */
            /*border: 1px solid black;*/
        }
"""

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
    QPushButton:pressed {
            background-color: #b1957f; /* Change background when pressed */
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
        border: 2px solid transparent;  /* Adds border to ScrollArea */
        border-radius: 5px;
    }
    
    QScrollBar:vertical {
        border: none;
        background: #d7cfc7;  /* Light beige background  #d7cfc7 */ 
        width: 12px;
        margin: 0px 0px 0px 0px;
        border-radius: 6px;  /* Rounds the entire scrollbar */
    }

    QScrollBar::handle:vertical {
         background: qlineargradient(                 
             x1:0, y1:0, x2:1, y2:1,                  
             /*stop:0 #A67C52, stop:1 #8B5E3C*/       
             stop:0 #83b6a0, stop:1 #74a28e           
         );                                           
        border: none;
        min-height: 20px;
        border-radius: 6px;  /* Rounded handle */
    }

    QScrollBar::handle:vertical:hover {
         background: qlineargradient(             
             x1:0, y1:0, x2:1, y2:1,              
             stop:0 #8bc1a9, stop:1 #7eb09a      
         );  /* Lighter brown when hovered */     
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

