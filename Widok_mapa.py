import folium
from PyQt6 import QtWidgets, QtWebEngineWidgets, QtCore
from LadowarkiM import Ladowarka


class Map:
    def __init__(self, DANE_2):
        super().__init__()
        self.__DANE_2 = DANE_2
        self.__map = folium.Map(location=[52.2297, 21.0122], zoom_start=6)
        self.__marker_group = folium.FeatureGroup()

        for ladowarka in self.__DANE_2.daj_ladowarki()[1500:]:
            x = ladowarka.daj_X()
            y = ladowarka.daj_Y()
            nazwa = ladowarka.daj_nazwa()
            self.__add_point(x, y, nazwa)

    def __add_point(self, lat, lon, name):
        marker = folium.Marker(location=[lat, lon], popup=name)
        self.__marker_group.add_child(marker)
        self.__map.add_child(self.__marker_group)

    def get_html(self):
        return self.__map.get_root().render()


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
        self.__pole_x = QtWidgets.QLineEdit(self)
        self.__pole_x.setPlaceholderText("Podaj X")
        self.__pole_y = QtWidgets.QLineEdit(self)
        self.__pole_y.setPlaceholderText("Podaj Y")
        self.__pole_nazwa = QtWidgets.QLineEdit(self)
        self.__pole_nazwa.setPlaceholderText("Podaj Nawa")

        # Dodanie pól tekstowych do layoutu
        text_layout.addWidget(self.__pole_x)
        text_layout.addWidget(self.__pole_y)
        text_layout.addWidget(self.__pole_nazwa)

        # Tworzenie przycisków
        self.__Dodawanie = QtWidgets.QPushButton('Dodaj stacje', self)
        self.__Dodawanie.clicked.connect(self.Dodaj_stacje)
        self.__Usuwanie = QtWidgets.QPushButton('Usun stacje', self)
        self.__Usuwanie.clicked.connect(self.Usun_stacje)

        # Dodanie przycisków do layoutu
        button_layout.addWidget(self.__Dodawanie)
        button_layout.addWidget(self.__Usuwanie)

        # Główny layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(text_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def Dodaj_stacje(self):
        self.__DANE_2.dodaj_ladowarke(Ladowarka(self.__pole_x.text(), self.__pole_y.text(), self.__pole_nazwa.text()))
        self.__wiget_glowny.przeladuj_mape()

    def Usun_stacje(self):
        self.__DANE_2.usun_ladowarke(Ladowarka(self.__pole_x.text(), self.__pole_y.text(), self.__pole_nazwa.text()))
        self.__wiget_glowny.przeladuj_mape()


class MapWidget(QtWidgets.QWidget):
    def __init__(self, DANE_2):
        super().__init__()
        self.__DANE_2 = DANE_2

        self.__map = Map(self.__DANE_2)
        self.__webview = QtWebEngineWidgets.QWebEngineView()
        self.__webview.setHtml(self.__map.get_html())
        self.__przyciski = Obsluga_mapy(self, self.__DANE_2, self.__map)
        self.__label = QtWidgets.QLabel("Stacje ładowania", self, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.__label.setStyleSheet("font-size: 30pt; font-family: Arial;")

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.__label, 0, 0)
        layout.addWidget(self.__webview, 1, 0)
        layout.addWidget(self.__przyciski, 2, 0)
        self.setLayout(layout)

    def przeladuj_mape(self):
        self.__map = Map(self.__DANE_2)
        new_html = self.__map.get_html()
        self.__webview.setHtml(new_html)
