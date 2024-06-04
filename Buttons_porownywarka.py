from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget
from PanstwaM import Lista_panstw


class Button_panstwo(QPushButton):
    def __init__(self, btn_name):
        super().__init__(btn_name)
        self.clicked.connect(self.klik)


    def klik(self):
        print(self.text())

class Buttons_lista_panstw(QWidget):
    def __init__(self):
        super().__init__()
        self.__buttons = []
        self.lista_panstw = Lista_panstw()

        for panstwo in self.lista_panstw:



