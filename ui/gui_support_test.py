from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QButtonGroup, QLabel

class ToggleButtonGroup(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Toggle Button Group")

        layout = QVBoxLayout()

        # Create a label to show the selected button
        self.label = QLabel("Selected: None")
        layout.addWidget(self.label)

        # Create a button group
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)  # Ensures only one button is checked at a time

        # Create toggle buttons
        self.btn1 = QPushButton("Option 1")
        self.btn1.setCheckable(True)

        self.btn2 = QPushButton("Option 2")
        self.btn2.setCheckable(True)

        self.btn3 = QPushButton("Option 3")
        self.btn3.setCheckable(True)

        # Add buttons to the group
        self.button_group.addButton(self.btn1, 1)
        self.button_group.addButton(self.btn2, 2)
        self.button_group.addButton(self.btn3, 3)

        # Connect the button group signal to a function
        self.button_group.buttonClicked[int].connect(self.button_clicked)

        # Add buttons to layout
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)

        self.setLayout(layout)

    def button_clicked(self, button_id):
        selected_button = self.button_group.button(button_id)
        self.label.setText(f"Selected: {selected_button.text()}")

# # Run the application
# app = QApplication([])
# window = ToggleButtonGroup()
# window.show()
# app.exec_()

if __name__ == '__main__':
    sigma = 5
    delta = 5
    n = ((1.645 + 1.28) * sigma / (delta - 1)) ** 2
    print(n)