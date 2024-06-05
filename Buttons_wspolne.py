from PyQt6.QtWidgets import QTabWidget, QPushButton, QVBoxLayout, QWidget
from Dane_IO import Fabryka_wejscia
from Buttons_porownywarka import Buttons_lista_panstw
from PanstwaM import Panstwo
from STALE import plik_z_danymi, DANE


class Buttons_trybow_panel(QTabWidget):
    def __init__(self):
        super().__init__()

        # Tworzenie widgetu dla pierwszej zakładki
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()

        tab1_layout.addWidget(Button_Wczytywanie())
        tab1.setLayout(tab1_layout)

        # Tworzenie widgetu dla drugiej zakładki
        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(Buttons_lista_panstw())
        tab2.setLayout(tab2_layout)

        tab3 = QWidget()
        tab3_layout = QVBoxLayout()
        tab3.setLayout(tab3_layout)

        # Dodawanie zakładek do widgetu
        self.addTab(tab1, "Wczytywanie")
        self.addTab(tab2, "Porownywarka")
        self.addTab(tab3, "Mapa")


class Button_Wczytywanie(QPushButton):
    def __init__(self):
        super().__init__("Wczytywanie")
        self.clicked.connect(self.klik)
        self.click_state = False

    def klik(self):
            self.setStyleSheet("background-color: green; color: white;")
            czytajnik = Fabryka_wejscia()
            czytajnik = czytajnik.daj_wejscie(plik_z_danymi)
            dane = czytajnik.czytaj()
            global DANE
            DANE.zamien_orginalne(dane)
            DANE.zamien_filtrowane(dane)