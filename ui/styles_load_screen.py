color_complete_normal = '#8cb7a4'
color_complete_press = '#6e8d7f'
color_ongoing_normal = '#728ea3'
color_ongoing_press = '#566b7a'
color_pending_normal = '#c4bd4e'
color_pending_press = '#9f9940'


storyline_container_style = """
    border: 2px solid gray;
    border-radius: 10px;
    font-size: 14px;
"""

quick_chat_button_style = """
    QPushButton {
            background-color: #8cb7a4;
            border-radius: 10px;
            border: none;
            padding: 25px;
            font-size: 25px;
            font-family: calibri;
            font-weight: bold;
        }
    QPushButton:pressed {
            background-color: #6e8d7f; /* Change background when pressed */
            border: 1px solid black;
        }
"""

lesson_button_style = '''
    QPushButton {
            background-color: %s;
            border-radius: 10px;
            border: none;
            text-align: left;
            padding: 20px
        }
    QPushButton:pressed {
            background-color: %s; /* Change background when pressed */
            border: 1px solid black;
        }
'''%(color_pending_normal, color_pending_press)

hide_lesson_button_style = """
    border: none;
    background: #e2d9d2;
"""

section_button_style = '''
    QPushButton {
            background-color: %s; /* #8cb7a4; */
            border-radius: 50px;
            border: None;
            font-size: 20px;
            font-weight: bold;
        }
    QPushButton:pressed {
            background-color: %s /* #6e8d7f;  Change background when pressed */
            /*border: 3px solid black;*/
        }
'''%(color_pending_normal, color_pending_press)

scrollbar_style = """
    QScrollArea {
        /* border: 2px solid transparent;  Adds border to ScrollArea */
        border: none;
        border-radius: 20px;
        background: #e2d9d2;
    }

    QScrollBar:vertical {
        border: none;
        background: #d7cfc7;  /* Light beige background  #d7cfc7 */ 
        width: 12px;
        margin: 0px 0px 0px 0px;        
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
         border: none;
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

section_lesson_container_style = """
    border-radius: 10px;
    background-color: #e2d9d2;
"""

scroll_content_style = """
    border: none;
    border-radius: 20px;
    background-color: #e2d9d2;
"""

def update_lesson_buttons_styles(button, mode):
    '''
    first bit - 0 - completed
    first bit - 1 - pending
    '''
    if mode == 0:
        temp_style = """
            QPushButton {
                    background-color: %s;
                    border-radius: 10px;
                    border: none;
                    text-align: left;
                    padding: 20px
                }
            QPushButton:pressed {
                    background-color: %s;       /* Change background when pressed */
                    border: 2px solid black;
                }
        """%(color_complete_normal, color_complete_press)
    elif mode == 1:
        temp_style = """
            QPushButton {
                    background-color: %s;
                    border-radius: 10px;
                    border: none;
                    text-align: left;
                    padding: 20px
                }
            QPushButton:pressed {
                    background-color: %s; /* Change background when pressed */
                    border: 2px solid black;
                }
        """%(color_pending_normal, color_pending_press)
    else:
        temp_style = ''
        print('mode not defined')

    button.setStyleSheet(temp_style)

def update_section_buttons_styles(button, mode):
    '''
    first bit - 0 - not selected
    first bit - 1 - selected
    second bit - 0 - complete
    second bit - 1 - ongoing
    second bit - 2 - pending
    '''
    if (mode == '00'):
        temp_style = """
            QPushButton {
                    background-color: %s; 
                    border-radius: 50px;
                    border: none;
                    font-size: 20px;
                    font-weight: bold;
                }
            QPushButton:pressed {
                    background-color: %s ;
        }
        """%(color_complete_normal, color_complete_press)
    elif (mode == '01'):
        temp_style = """
                    QPushButton {
                            background-color: %s; 
                            border-radius: 50px;
                            border: none;
                            font-size: 20px;
                            font-weight: bold;
                        }
                    QPushButton:pressed {
                            background-color: %s; 
                }
                """%(color_ongoing_normal, color_ongoing_press)
    elif (mode == '02'):
        temp_style = """
                    QPushButton {
                            background-color: %s; 
                            border-radius: 50px;
                            border: none;
                            font-size: 20px;
                            font-weight: bold;
                        }
                    QPushButton:pressed {
                            background-color: %s; 
                }
                """%(color_pending_normal, color_pending_press)
    elif (mode == '10'):
        temp_style = """
                    QPushButton {
                            background-color: %s; 
                            border-radius: 50px;
                            border: 3px solid black;
                            font-size: 20px;
                            font-weight: bold;
                        }
                    QPushButton:pressed {
                            background-color: %s; 
                            border: 3px solid black;
                }
                """%(color_complete_normal, color_complete_press)
    elif (mode == '11'):
        temp_style = """
                    QPushButton {
                            background-color: %s; 
                            border-radius: 50px;
                            border: 3px solid black;
                            font-size: 20px;
                            font-weight: bold;
                        }
                    QPushButton:pressed {
                            background-color: %s ;
                            border: 3px solid black;
                }
                """%(color_ongoing_normal, color_ongoing_press)
    elif (mode == '12'):
        temp_style = """
                    QPushButton {
                            background-color: %s; 
                            border-radius: 50px;
                            border: 3px solid black;
                            font-size: 20px;
                            font-weight: bold;
                        }
                    QPushButton:pressed {
                            background-color: %s ;
                            border: 3px solid black;
                }
                """%(color_pending_normal, color_pending_press)
    else:
        temp_style = ''
        print('mode not defined')

    button.setStyleSheet(temp_style)



