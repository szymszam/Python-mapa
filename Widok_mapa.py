import folium
from PyQt6 import QtWidgets, QtWebEngineWidgets
from LadowarkiM import Ladowarka
from Dane_IO import Fabryka_wejscia_mapa, Wejscie_txt_mapa
import sys

class Map:
    def __init__(self, DANE_2):
        self.__DANE_2 = DANE_2
        self.map = folium.Map(location=[52.2297, 21.0122], zoom_start=6)
        self.marker_group = folium.FeatureGroup()

        for ladowarka in self.__DANE_2.daj_ladowarki()[2700:]:
            x = ladowarka.daj_X()
            y = ladowarka.daj_Y()
            nazwa = ladowarka.daj_nazwa()
            self.add_point(x, y, nazwa)


    def add_point(self, lat, lon, name):
        marker = folium.Marker(location=[lat, lon], popup=name)
        self.marker_group.add_child(marker)
        self.map.add_child(self.marker_group)

    def get_html(self):
        return self.map.get_root().render()


class Obsluga_mapy(QtWidgets.QWidget):
        def __init__(self, wiget_glowny, DANE_2, Mapa):
            super().__init__()
            self.__wiget_glowny = wiget_glowny
            self.__DANE_2 = DANE_2
            self.__Mapa = Mapa

            # Layouty poziome dla pól tekstowych i przycisków
            text_layout = QtWidgets.QHBoxLayout()
            button_layout = QtWidgets.QHBoxLayout()

            # Tworzenie pól tekstowych
            self.pole_x = QtWidgets.QLineEdit(self)
            self.pole_x.setPlaceholderText("Podaj X")
            self.pole_y = QtWidgets.QLineEdit(self)
            self.pole_y.setPlaceholderText("Podaj Y")
            self.pole_nazwa = QtWidgets.QLineEdit(self)
            self.pole_nazwa.setPlaceholderText("Podaj Nawa")

            # Dodanie pól tekstowych do layoutu
            text_layout.addWidget(self.pole_x)
            text_layout.addWidget(self.pole_y)
            text_layout.addWidget(self.pole_nazwa)

            # Tworzenie przycisków
            self.Dodawanie = QtWidgets.QPushButton('Dodaj stacje', self)
            self.Dodawanie.clicked.connect(self.Dodaj_stacje)
            self.Usuwanie = QtWidgets.QPushButton('Usun stacje', self)
            self.Usuwanie.clicked.connect(self.Usun_stacje)

            # Dodanie przycisków do layoutu
            button_layout.addWidget(self.Dodawanie)
            button_layout.addWidget(self.Usuwanie)

            # Główny layout
            main_layout = QtWidgets.QVBoxLayout()
            main_layout.addLayout(text_layout)
            main_layout.addLayout(button_layout)

            self.setLayout(main_layout)

        def Dodaj_stacje(self):
            self.__DANE_2.dodaj_ladowarke(Ladowarka(self.pole_x.text(), self.pole_y.text(), self.pole_nazwa.text()))
            self.__wiget_glowny.przeladuj_mape()


        def Usun_stacje(self):
            self.__DANE_2.usun_ladowarke(Ladowarka(self.pole_x.text(), self.pole_y.text(), self.pole_nazwa.text()))
            self.__wiget_glowny.przeladuj_mape()

class MapWidget(QtWidgets.QWidget):
    def __init__(self, DANE_2):
        super().__init__()
        self.__DANE_2 = DANE_2

        self.__map = Map(self.__DANE_2)
        self.__webview = QtWebEngineWidgets.QWebEngineView()
        self.__webview.setHtml(self.__map.get_html())
        self.przyciski = Obsluga_mapy(self, self.__DANE_2, self.__map)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.__webview, 0, 0)
        layout.addWidget(self.przyciski, 1, 0)
        self.setLayout(layout)

    def przeladuj_mape(self):
        self.__map = Map(self.__DANE_2)
        new_html = self.__map.get_html()
        self.__webview.setHtml(new_html)
