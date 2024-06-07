import folium
import sys
from PyQt5 import QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QWidget

class Mapa:
    def __init__(self):
        self.map = folium.Map(location=[52.237049, 19.017532], zoom_start=6)
        self.marker_group = folium.FeatureGroup()

    def dodaj_punktM(self, X, Y, name):
        marker = folium.Marker(location=[X, Y], popup=name)
        self.marker_group.add_child(marker)
        self.map.add_child(self.marker_group)

    def usun_punktM(self):
        self.marker_group.clear_layers()

    def daj_html(self):
        return self.map.get_root().render()

class WidgetMapy(QWidget):
    def __init__(self):
        super().__init__()
        self.mapa = Mapa()
        self.widok = QtWebEngineWidgets.QWebEngineView()
        self.widok.setHtml(self.mapa.daj_html())
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.widok)

    def dodaj_punkt(self):
        cords = self.cords_input.text()
        name = self.name_input.text()
        if cords and name:
            X, Y = map(float, cords.split(','))
            self.mapa.dodaj_punktM(X, Y, name)
            self.widok.setHtml(self.mapa.daj_html())
            self.cords_input.clear()
            self.name_input.clear()
    def usun_punkt(self):
        self.mapa.usun_punktM()
        self.widok.setHtml(self.mapa.daj_html())