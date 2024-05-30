from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget


class Button_panstwo(QPushButton):
    def __init__(self, label):
        super().__init__(label)
        self.clicked.connect(self.klik)

    def klik(self):
        print(self.text())

class Buttons_lista_panstw(QWidget):
    def __init__(self):
        super().__init__()
        self.__init_btns_p()

    def __init_btns_p(self):

        layout = QVBoxLayout()
        buttons = ["Przycisk 1", "Przycisk 2", "Przycisk 3", "Przycisk 4"]
        for button_label in buttons:
            button = Button_panstwo(button_label)
            layout.addWidget(button)
        self.setLayout(layout)