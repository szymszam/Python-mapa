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
        przyciski = []
        dane = DANE.daj_filtrowane()
        dane = dane.daj_panstwa()
        for i in range(len(dane)):
            tytul = dane[i].daj_nazwa()
            przyciski.append(Button_panstwo(tytul))

        layout = QVBoxLayout()

        for btn in przyciski:
            layout.addWidget(btn)

        self.setLayout(layout)

