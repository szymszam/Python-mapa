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
        self.__lista_panstw = Lista_panstw()  # tutAJ BEDZIE Z FILTROWANIE TO DO

        self.__lista = self.__lista_panstw.daj_panstwa()

        for i in range(len(self.__lista)):
            self.__buttons.append(Button_panstwo(self.__lista[i].daj_nazwa()))
            print("Dodaje przycisk")

        layout = QVBoxLayout()

        for btn in self.__buttons:
            layout.addWidget(btn)

        self.setLayout(layout)

