from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget
from Dane_IO import Fabryka_wejscia, Wejscie_xlsx
from PanstwaM import Panstwo, Lista_panstw
from STALE import plik_z_danymi, DANE


class Button_panstwo(QPushButton):
    def __init__(self, btn_name):
        super().__init__(btn_name)
        self.clicked.connect(self.klik)

    def klik(self):
        print(self.text())



class Buttons_lista_panstw(QWidget):
    def __init__(self):
        super().__init__()
        self.__przyciski = []
        global DANE
        self.__dane = DANE.daj_filtrowane()
        self.__dane = self.__dane.daj_panstwa()
        self.stworz_przyciski()
    def stworz_przyciski(self):
        for i in range(len(self.__dane)):
            tytul = self.__dane[i].daj_nazwa()
            self.__przyciski.append(Button_panstwo(tytul))

        layout = QVBoxLayout()

        for btn in self.__przyciski:
            layout.addWidget(btn)

        self.setLayout(layout)

