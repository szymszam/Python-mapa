from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget
from Dane_IO import Fabryka_wejscia, Wejscie_xlsx
from PanstwaM import Panstwo, Lista_panstw
from STALE import plik_z_danymi

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
        czytajnik = Fabryka_wejscia()
        czytaj_xlsx = czytajnik.daj_wejscie( plik_z_danymi)
        lista = czytaj_xlsx.czytaj()

        self.__lista_panstw = lista  # tutAJ BEDZIE Z FILTROWANIE TO DO

        self.__lista = self.__lista_panstw.daj_panstwa()

        for i in range(len(self.__lista)):
            self.__buttons.append(Button_panstwo(self.__lista[i].daj_nazwa()))
            print("Dodaje przycisk")

        layout = QVBoxLayout()

        for btn in self.__buttons:
            layout.addWidget(btn)

        self.setLayout(layout)

