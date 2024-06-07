import folium
import sys
from PyQt5 import QtWidgets, QtWebEngineWidgets

class Map:
    def __init__(self):
        self.map = folium.Map(location=[52.237049, 19.017532], zoom_start=6)
        self.marker_group = folium.FeatureGroup()

    def add_point(self, lat, lon, name):
        marker = folium.Marker(location=[lat, lon], popup=name)
        self.marker_group.add_child(marker)
        self.map.add_child(self.marker_group)

    def remove_all_points(self):
        self.marker_group.clear_layers()

    def get_html(self):
        return self.map.get_root().render()



class MapWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.map = Map()
        self.webview = QtWebEngineWidgets.QWebEngineView()
        self.webview.setHtml(self.map.get_html())

        self.coords_input = QtWidgets.QLineEdit()
        self.name_input = QtWidgets.QLineEdit()
        self.add_button = QtWidgets.QPushButton("Dodaj punkt")
        self.add_button.clicked.connect(self.add_point)

        self.remove_button = QtWidgets.QPushButton("Usuń wszystkie punkty")
        self.remove_button.clicked.connect(self.remove_all_points)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.webview)
        layout.addWidget(QtWidgets.QLabel("Współrzędne (X, Y):"))
        layout.addWidget(self.coords_input)
        layout.addWidget(QtWidgets.QLabel("Nazwa Ładowarki:"))
        layout.addWidget(self.name_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)

        self.setLayout(layout)

    def add_point(self):
        coords = self.coords_input.text()
        name = self.name_input.text()
        if coords and name:
            lat, lon = map(float, coords.split(','))
            self.map.add_point(lat, lon, name)
            self.webview.setHtml(self.map.get_html())
            self.coords_input.clear()
            self.name_input.clear()

    def remove_all_points(self):
        self.map.remove_all_points()
        self.webview.setHtml(self.map.get_html())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QMainWindow()
    window.setWindowTitle("Mapa z PyQt5 i Folium")
    window.setGeometry(100, 100, 800, 600)

    map_widget = MapWidget()
    window.setCentralWidget(map_widget)

    window.show()
    sys.exit(app.exec_())