from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget, QLineEdit
from PanstwaM import Panstwo, Lista_panstw, Lista_panstw_z_filtowaniem
from STALE import DANE

#Przycisk reprezentujący pojedyńcze państwo
class Button_panstwo(QPushButton):
    def __init__(self, panstwo_reprezentowane, referencja_do_wykresu):
        super().__init__(panstwo_reprezentowane.daj_nazwa())
        self.__wykres = referencja_do_wykresu
        self.__panstwo_reprezentowane = panstwo_reprezentowane
        self.clicked.connect(self.klik)
        if self.__panstwo_reprezentowane in DANE.daj_zaznaczone().daj_panstwa():
            self.setStyleSheet("background-color: lightblue; color: white;")
            self.click_state = True
        else:
            self.click_state = False

    def klik(self):
        podglad = DANE.daj_zaznaczone().daj_panstwa()

        if self.__panstwo_reprezentowane not in podglad:
             podglad.append(self.__panstwo_reprezentowane)
             DANE.zamien_zaznaczone(Lista_panstw(podglad))

        elif self.__panstwo_reprezentowane in podglad:
              podglad.remove(self.__panstwo_reprezentowane)
              DANE.zamien_zaznaczone(Lista_panstw(podglad))

        self.click_state = not self.click_state
        if self.click_state == True:
            self.setStyleSheet("background-color: lightblue; color: white;")

        else:
            self.setStyleSheet("")

        self.__wykres.zaladuj_wykres()




#Wiget zawierający przyciski państw pod searchbarem
class Buttons_lista_panstw(QWidget):
    def __init__(self, odwolanie_do_wykresu):
        super().__init__()
        self.__wykres = odwolanie_do_wykresu
        self.stworz_przyciski()


    def stworz_przyciski(self):
        dane = DANE.daj_filtrowane().daj_panstwa()
        przyciski = []

        for i in range(len(dane)):
            przyciski.append(Button_panstwo(dane[i], self.__wykres))

        layout = QVBoxLayout()
        for btn in przyciski:
            btn.setFixedSize(100,18)
            layout.addWidget(btn)

        self.setLayout(layout)

#Wiget zawierający searchbar i przycisk do niego
class Searchbar(QWidget):
    def __init__(self, panel_glowny=None):
        super().__init__()
        self.stworz_searchbar("Wpisz termin")
        self.__panel_glowny = panel_glowny


    #tworzy searchbar i guzik
    def stworz_searchbar(self, placeholder_text):
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(placeholder_text)
        self.save_button = QPushButton("Szukaj")
        self.save_button.clicked.connect(self.filtruj_searchbar)

        layout = QVBoxLayout()
        self.save_button.setFixedSize(100,20)
        self.line_edit.setFixedSize(100,20)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

    #funkcja dzialajaca po kjliknieciu guzika szukaj aktualnie zmienia wartosc DANE.panstwa_filtowane
    def filtruj_searchbar(self):
        temp = DANE.daj_filtrowane()
        temp = Lista_panstw_z_filtowaniem(temp)
        temp.filtruj_liste(self.line_edit.text(), DANE.daj_orginalne().daj_panstwa())
        DANE.zamien_filtrowane(temp)
        self.__panel_glowny.wyczysc_tab2()
        self.__panel_glowny.zapelnij_tab2()

