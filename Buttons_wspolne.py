from PyQt6.QtWidgets import QTabWidget, QPushButton, QVBoxLayout, QWidget
from Dane_IO import xlsx_czytaj_wykres


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
        self.xlsx_czytaj = xlsx_czytaj_wykres()

    def klik(self):
        self.click_state = not self.click_state
        if self.click_state == True:
            print("tutaj bedzie odwolanie do wczytywanie xlsx i txt")
            self.setStyleSheet("background-color: green; color: white;")
            #self.xlsx_czytaj.czytaj(r"C:\Users\olech\Desktop\road_eqr_carpda_spreadsheet.xlsx") #Tutaj miejsce do podania linku

        else:
            self.setStyleSheet("background-color: red; color: white;")
