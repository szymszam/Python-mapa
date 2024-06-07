from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
import sys
import folium


class MapWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        self.map_view = QWebEngineView(self)
        layout.addWidget(self.map_view)

        # Tworzenie mapy za pomocą biblioteki Folium
        map_obj = folium.Map(location=[51.5074, -0.1278], zoom_start=10)

        # Dodawanie punktów na mapie
        folium.Marker(location=[51.5074, -0.1278], popup='London').add_to(map_obj)
        folium.Marker(location=[48.8566, 2.3522], popup='Paris').add_to(map_obj)

        # Konwertowanie mapy do HTML
        map_html = map_obj.get_root().render()

        # Wczytywanie mapy do QWebEngineView
        self.map_view.setHtml(map_html)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapWidget()
    window.setGeometry(100, 100, 800, 600)
    window.setWindowTitle("Map Viewer")
    window.show()
    sys.exit(app.exec())
