import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grupowany Wykres Kolumnowy w PyQt6")

        # Dane do wykresu
        labels = ['A', 'B', 'C', 'D', 'E']
        category1 = [23, 45, 56, 78, 89]
        category2 = [34, 23, 54, 67, 90]
        category3 = [15, 35, 45, 60, 70]

        x = np.arange(len(labels))  # etykiety lokalizacji
        width = 0.2  # szerokość słupków

        sc = MplCanvas(self, width=5, height=4, dpi=100)

        # Rysowanie słupków dla każdej kategorii
        sc.ax.bar(x - width, category1, width, label='Kategoria 1')
        sc.ax.bar(x, category2, width, label='Kategoria 2')
        sc.ax.bar(x + width, category3, width, label='Kategoria 3')

        # Dodawanie etykiet i tytułu
        sc.ax.set_xlabel('Kategorie')
        sc.ax.set_ylabel('Wartości')
        sc.ax.set_title('Grupowany Wykres Kolumnowy')
        sc.ax.set_xticks(x)
        sc.ax.set_xticklabels(labels)
        sc.ax.legend()

        # Tworzenie centralnego widgetu
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.addWidget(sc)
        central_widget.setLayout(layout)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
