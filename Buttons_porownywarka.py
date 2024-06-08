from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget, QLineEdit, QGridLayout, QHBoxLayout, QSlider
from PanstwaM import Lista_panstw, Lista_panstw_z_filtowaniem


# Przycisk reprezentujący pojedyncze państwo
class Button_panstwo(QPushButton):
    def __init__(self, panstwo_reprezentowane, referencja_do_wykresu, DANE_1):
        super().__init__(panstwo_reprezentowane.daj_nazwa())
        self.__wykres = referencja_do_wykresu
        self.__panstwo_reprezentowane = panstwo_reprezentowane
        self.__DANE_1 = DANE_1
        self.setFixedSize(400, 900)
        self.clicked.connect(self.klik)

        if self.__panstwo_reprezentowane in self.__DANE_1.daj_zaznaczone().daj_panstwa():
            self.setStyleSheet("background-color: lightblue; color: white;")
            self.click_state = True
        else:
            self.click_state = False

    def klik(self):
        podglad = self.__DANE_1.daj_zaznaczone().daj_panstwa()

        if self.__panstwo_reprezentowane not in podglad and len(podglad) < 3:
            podglad.append(self.__panstwo_reprezentowane)
            self.__DANE_1.zamien_zaznaczone(Lista_panstw(podglad))
            self.click_state = not self.click_state

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
            btn.setFixedSize(100, 37)  # Ustawia rozmiar przycisku
            layout.addWidget(btn, row, col)

            col += 1
            if col >= 3:  # Ustawia przyciski w trzech kolumnach
                col = 0
                row += 1

        self.setLayout(layout)


class Szukaj_i_zapisz(QWidget):
    def __init__(self, panel_glowny=None, DANE_1=None, Wykres=None):
        super().__init__()
        self.__panel_glowny = panel_glowny
        self.__DANE_1 = DANE_1
        self.__Wykres = Wykres
        self.setFixedSize(400, 50)

        self.stworz()

    def stworz(self):
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Wpisz termin")
        self.line_edit.setFixedSize(130, 30)

        self.przycisk_szukaj = QPushButton("Szukaj")
        self.przycisk_szukaj.clicked.connect(self.filtruj_searchbar)
        self.przycisk_szukaj.setFixedSize(100, 30)

        self.przycisk_zapisz = Przycisk_zapisu(self.__Wykres)
        self.przycisk_zapisz.setFixedSize(70, 30)

        layout = QHBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.przycisk_szukaj)
        layout.addWidget(self.przycisk_zapisz)
        self.setLayout(layout)

    def filtruj_searchbar(self):
        temp = self.__DANE_1.daj_filtrowane()
        temp = Lista_panstw_z_filtowaniem(temp)
        temp.filtruj_liste(self.line_edit.text(), self.__DANE_1.daj_orginalne().daj_panstwa())
        self.__DANE_1.zamien_filtrowane(temp)
        self.__panel_glowny.wyczysc_tab2()
        self.__panel_glowny.zapelnij_bts_panstwa_tab2()


class Przycisk_zapisu(QPushButton):
    def __init__(self, wykres):
        super().__init__("Zapisz")
        self.__wykres = wykres
        self.clicked.connect(self.__zapisz)

    def __zapisz(self):
        self.__wykres.zapisz_wykres_jako_pdf()


class Suwaki_lat(QWidget):
    def __init__(self, DANE_1, Wykres):
        super().__init__()
        self.__DANE_1 = DANE_1
        self.__wykres = Wykres
        self.stworz_suwaki()

    def stworz_suwaki(self):
        self.min_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.min_slider.setMinimum(0)
        self.min_slider.setMaximum(len(self.__DANE_1.daj_orginalne().daj_panstwa()[0].daj_ilosc()))
        self.min_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.min_slider.setTickInterval(len(self.__DANE_1.daj_orginalne().daj_panstwa()[0].daj_ilosc()))
        self.min_slider.valueChanged.connect(self.updateMinValue)

        self.max_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.max_slider.setMinimum(0)
        self.max_slider.setMaximum(len(self.__DANE_1.daj_orginalne().daj_panstwa()[0].daj_ilosc()))
        self.max_slider.setValue(len(self.__DANE_1.daj_orginalne().daj_panstwa()[0].daj_ilosc()))
        self.max_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.max_slider.setTickInterval(len(self.__DANE_1.daj_orginalne().daj_panstwa()[0].daj_ilosc()))
        self.max_slider.valueChanged.connect(self.updateMaxValue)

        layout = QVBoxLayout()
        layout.addWidget(self.min_slider)
        layout.addWidget(self.max_slider)

        self.setLayout(layout)

    def updateMinValue(self, wartosc):
        max_war = self.max_slider.value()
        if wartosc > max_war:
            self.min_slider.setValue(max_war)
        self.__DANE_1.zmien_pier_rok(wartosc)
        self.__wykres.zaladuj_wykres()

    def updateMaxValue(self, wartosc):
        min_war = self.min_slider.value()
        if wartosc < min_war:
            self.max_slider.setValue(min_war)
        self.__DANE_1.zmien_ost_rok(wartosc)
        self.__wykres.zaladuj_wykres()
