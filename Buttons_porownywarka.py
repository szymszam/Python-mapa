from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget, QLineEdit
from Dane_IO import Fabryka_wejscia, Wejscie_xlsx
from PanstwaM import Panstwo, Lista_panstw, Lista_panstw_z_filtowaniem
from STALE import DANE

#Przycisk reprezentujący pojedyńcze państwo
class Button_panstwo(QPushButton):
    def __init__(self, panstwo_reprezentowane):
        super().__init__(panstwo_reprezentowane.daj_nazwa())
        self.__panstwo_reprezentowane = panstwo_reprezentowane #Obiekt panstwa które reprezentuje
        self.clicked.connect(self.klik)

    def klik(self):
        podglad = DANE.daj_zaznaczone().daj_panstwa()

        if self.__panstwo_reprezentowane not in podglad:
            podglad.append(self.__panstwo_reprezentowane)
            DANE.zamien_zaznaczone(Lista_panstw(podglad))

        elif self.__panstwo_reprezentowane in podglad:
            podglad.remove(self.__panstwo_reprezentowane)
            DANE.zamien_zaznaczone(Lista_panstw(podglad))

        for panstwo in DANE.daj_zaznaczone().daj_panstwa():
            print(panstwo)
        print("----------------------")





#Wiget zawierający przyciski państw pod searchbarem
class Buttons_lista_panstw(QWidget):
    def __init__(self):
        super().__init__()
        self.stworz_przyciski()

    def stworz_przyciski(self):
        dane = DANE.daj_filtrowane().daj_panstwa()
        przyciski = []

        for i in range(len(dane)):
            przyciski.append(Button_panstwo(dane[i]))

        layout = QVBoxLayout()
        for btn in przyciski:
            layout.addWidget(btn)

        self.setLayout(layout)

#Wiget zawierający searchbar i przycisk do niego
class Searchbar(QWidget):
    def __init__(self, placeholder_text="Wpisz termin"):
        super().__init__()
        self.stworz_searchbar(placeholder_text)

    #tworzy searchbar i guzik
    def stworz_searchbar(self, placeholder_text):
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(placeholder_text)
        self.save_button = QPushButton("Szukaj")
        self.save_button.clicked.connect(self.filtruj_searchbar)

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

    #funkcja dzialajaca po kjliknieciu guzika szukaj aktualnie zmienia wartosc DANE.panstwa_filtowane
    def filtruj_searchbar(self):
        temp = DANE.daj_filtrowane()
        temp = Lista_panstw_z_filtowaniem(temp)
        temp.filtruj_liste(self.line_edit.text(), DANE.daj_orginalne().daj_panstwa())
        DANE.zamien_filtrowane(temp)
        for panstwo in DANE.daj_filtrowane().daj_panstwa():
            print(panstwo.daj_nazwa())
        print("--------------------------")
