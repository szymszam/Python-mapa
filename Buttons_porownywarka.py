import sys
from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget, QLineEdit, QGridLayout
from PanstwaM import Lista_panstw, Lista_panstw_z_filtowaniem

# Przycisk reprezentujący pojedyncze państwo
class Button_panstwo(QPushButton):
    def __init__(self, panstwo_reprezentowane, referencja_do_wykresu, DANE_1):
        super().__init__(panstwo_reprezentowane.daj_nazwa())
        self.__wykres = referencja_do_wykresu
        self.__panstwo_reprezentowane = panstwo_reprezentowane
        self.__DANE_1 = DANE_1

        self.clicked.connect(self.klik)

        if self.__panstwo_reprezentowane in self.__DANE_1.daj_zaznaczone().daj_panstwa():
            self.setStyleSheet("background-color: lightblue; color: white;")
            self.click_state = True
        else:
            self.click_state = False

    def klik(self):
        podglad = self.__DANE_1.daj_zaznaczone().daj_panstwa()

        if self.__panstwo_reprezentowane not in podglad:
             podglad.append(self.__panstwo_reprezentowane)
             self.__DANE_1.zamien_zaznaczone(Lista_panstw(podglad))

        elif self.__panstwo_reprezentowane in podglad:
              podglad.remove(self.__panstwo_reprezentowane)
              self.__DANE_1.zamien_zaznaczone(Lista_panstw(podglad))

        self.click_state = not self.click_state
        if self.click_state == True:
            self.setStyleSheet("background-color: lightblue; color: white;")

        else:
            self.setStyleSheet("")

        self.__wykres.zaladuj_wykres()


# Wiget zawierający przyciski państw pod searchbarem
class Buttons_lista_panstw(QWidget):
    def __init__(self, odwolanie_do_wykresu, DANE_1):
        super().__init__()
        self.__wykres = odwolanie_do_wykresu
        self.__DANE_1 = DANE_1
        self.stworz_przyciski()


    def stworz_przyciski(self):
        dane = self.__DANE_1.daj_filtrowane().daj_panstwa()

        layout = QGridLayout()  # Użyjemy siatki do umieszczania przycisków

        row = 0
        col = 0
        for i in range(len(dane)):
            btn = Button_panstwo(dane[i], self.__wykres, self.__DANE_1)
            btn.setFixedSize(100, 37)  # Ustawia rozmiar przycisku na 75% oryginalnej wartości
            layout.addWidget(btn, row, col)

            col += 1
            if col >= 2:  # Ustawia przyciski w dwóch kolumnach
                col = 0
                row += 1

        self.setLayout(layout)


# Widget zawierający searchbar i przycisk do niego
class Searchbar(QWidget):
    def __init__(self, panel_glowny=None, DANE_1=None):
        super().__init__()
        self.stworz_searchbar("Wpisz termin")
        self.__panel_glowny = panel_glowny
        self.__DANE_1 = DANE_1


    # Tworzy searchbar i guzik
    def stworz_searchbar(self, placeholder_text):
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText(placeholder_text)
        self.save_button = QPushButton("Szukaj")
        self.save_button.clicked.connect(self.filtruj_searchbar)

        layout = QVBoxLayout()
        self.save_button.setFixedSize(100, 50)  # Ustawia rozmiar przycisku
        self.line_edit.setFixedSize(100, 50)  # Ustawia rozmiar searchbara
        layout.addWidget(self.line_edit)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

    #funkcja dzialajaca po kjliknieciu guzika szukaj aktualnie zmienia wartosc DANE.panstwa_filtowane
    def filtruj_searchbar(self):
        temp = self.__DANE_1.daj_filtrowane()
        temp = Lista_panstw_z_filtowaniem(temp)
        temp.filtruj_liste(self.line_edit.text(), self.__DANE_1.daj_orginalne().daj_panstwa())
        self.__DANE_1.zamien_filtrowane(temp)
        self.__panel_glowny.wyczysc_tab2()
        self.__panel_glowny.zapelnij_bts_panstwa_tab2()
