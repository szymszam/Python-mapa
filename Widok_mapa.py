import folium
from PyQt6 import QtWidgets, QtWebEngineWidgets
from Dane_IO import Fabryka_wejscia_mapa, Wejscie_txt_mapa
import sys

class Map:
    def __init__(self, Lista_ladowarek=[]):
        self.__Lista_ladowarek = Lista_ladowarek.daj_ladowarki()
        self.map = folium.Map(location=[52.2297, 21.0122], zoom_start=6)
        self.marker_group = folium.FeatureGroup()
        for ladowarka in self.__Lista_ladowarek[:500]:
            X, Y = ladowarka.daj_lokacje()
            Nazwa = ladowarka.daj_nazwa()
            self.add_point(X, Y, Nazwa)


    def add_point(self, lat, lon, name):
        marker = folium.Marker(location=[lat, lon], popup=name)
        self.marker_group.add_child(marker)
        self.map.add_child(self.marker_group)

    def remove_all_points(self):
        self.marker_group.clear_layers()

    def get_html(self):
        return self.map.get_root().render()


class Obsluga_mapy(QtWidgets.QWidget):
        def __init__(self):
            super().__init__()

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
            print("Dodaje")

        def Usun_stacje(self):
            print("spijasz")

class MapWidget(QtWidgets.QWidget):
    def __init__(self, Obiekt_lista_ladowarek):
        super().__init__()

        self.map = Map(Obiekt_lista_ladowarek)
        self.webview = QtWebEngineWidgets.QWebEngineView()
        self.webview.setHtml(self.map.get_html())
        self.przyciski = Obsluga_mapy()



        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.webview)
        layout.addWidget(self.przyciski)
        self.setLayout(layout)


# if __name__ == "__main__":
#     Fabryka = Fabryka_wejscia_mapa()
#     czytajnik = Fabryka.daj_wejscie(r"C:\Users\User\Desktop\stacje_ładowania_pojazdów_projekt_2024L\stacje.txt")
#     Ladowarki = czytajnik.czytaj()
#     app = QtWidgets.QApplication(sys.argv)
# 
#     window = QtWidgets.QMainWindow()
#     window.setWindowTitle("Mapa z PyQt6 i Folium")
#     window.setGeometry(100, 100, 800, 600)
# 
#     map_widget = MapWidget(Ladowarki)
#     window.setCentralWidget(map_widget)
# 
#     window.show()
#     sys.exit(app.exec())