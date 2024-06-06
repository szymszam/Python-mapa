import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QWidget, QVBoxLayout


class ChartWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Utwórz układ pionowy
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        # Utwórz obiekt figury i oś
        self.figure, self.ax = plt.subplots()

        # Utwórz kanvas dla figury
        self.canvas = FigureCanvas(self.figure)

        # Dodaj kanvas do układu
        layout.addWidget(self.canvas)

        # Ustawanie tytułów
        self.ax.set_title("Wykres")
        self.ax.set_xlabel("Oś X")
        self.ax.set_ylabel("Oś Y")

        # Inicjalizuj dane
        self.categories = ['A', 'B', 'C', 'D', 'E']
        self.values = [10, 20, 15, 25, 30]

        # Dodaj przykładowe dane do wykresu
        self.update_chart()

    def update_chart(self):
        # Usuń poprzednie dane
        self.ax.clear()

        # Dodaj nowe dane
        self.ax.bar(self.categories, self.values)

        # Odśwież wykres
        self.canvas.draw()
