background_color = '#3B4252'
inputbackground = '#8cb7a4'


label_style = '''
    border: none;
    font-weight: bold;
    font-size: 14px;
    padding: 0px;
'''


input_style = '''
    QLineEdit{
        background-color: #8cb7a4;
        border: 2px solid #4C566A;
        border-radius: 5px;
        padding: 5px;
        color: black;
        font-weight: bold;
        font-size: 14px;
    }
    
    QLineEdit:focus {
        border: 2px solid #393939;
    }
'''


login_button_style = '''
    QPushButton {
        background-color: #6889b1;
        border: none;
        border-radius: 10px;
        padding: 8px;
        font-weight: bold;
        height: 50px;
        font-size: 18px;
    }
    
    QPushButton:hover {
        background-color: #577ba8;
    }

    QPushButton:pressed {
        background-color: #4e6f97;
    }
'''


borderless_button_style = '''
    QPushButton {
        background-color: #8cb7a4;
        border: none;
        padding: 8px;
        font-weight: bold;
        font-size: 14px;
    }
    
    QPushButton:hover {
        color: #0000CD;
    }

    QPushButton:pressed {
        color: navy;
        font-weight: bold
    }
'''


login_container_style = '''
    QFrame {
        background-color: #8cb7a4;
        border-radius: 15px;
        padding: 20px;
    }
'''


error_label_style = '''
    color: red;
    border: none;
    margin: 0px;
    padding: 0px;
    font-size: 14px;
    background-color: #8cb7a4;
'''


signup_label_style = '''
    border: none;
    padding: 0px;
    color: black;
    font-size: 14px;
    font-weight: bold;
'''


signup_button_style = '''
    QPushButton {
        background-color: #5E81AC;
        border: none;
        border-radius: 10px;
        padding: 8px;
        font-weight: bold;
        height: 40px;
        font-size: 18px;
    }
    
    QPushButton:hover {
        background-color: #81A1C1;
    }

    QPushButton:pressed {
        background-color: #88C0D0;
    }
'''


signup_entry_style = '''
    QLineEdit{
        background-color: #8cb7a4;
        border: 2px solid #4C566A;
        border-radius: 5px;
        padding: 5px;
        color: black;
        font-weight: bold;
        font-size: 14px;
    }
    
    QLineEdit:focus {
        border: 2px solid #393939;
    }
    
    QLineEdit:disabled{
        border: 2px solid #616060;
        color: #616060;
    }
    
'''


signup_radio_button_style = '''
    background-color: #8cb7a4;
'''


password_view_button_style = '''
    QPushButton {
        background-color: transparent;
        border-radius: 5px;
    }
    
    QPushButton:hover {
        background-color: #81A1C1;
    }
    
    QPushButton:pressed { 
        background-color: #699582;
    }
'''

signup_details_frame_style = """
    QFrame { 
        border: 1px solid #5E81AC; 
        padding: 10px; 
        margin: 0px;
    }
"""

resend_otp_button_style = '''
    QPushButton {
        background-color: #5E81AC;
        border: none;
        border-radius: 10px;
        padding: 8px;
        height: 20px;
        font-size: 14px;
    }

    QPushButton:hover {
        background-color: #81A1C1;
    }

    QPushButton:pressed {
        background-color: #88C0D0;
    }
    
    QPushButton:disabled {
        background-color: #cacaca;
    }
'''