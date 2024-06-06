import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from STALE import DANE


class Wykres(QWidget):
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
        self.ax.set_xlabel("Lata")
        self.ax.set_ylabel("Liczba aut")

        # Inicjalizuj dane
        self.__Panstwa = {}  # Słownik przechowujący serie danych {label: (categories, values)}

        # Dodaj przykładowe dane do wykresu
        self.zaladuj_wykres()


    def zaladuj_wykres(self):
        self.__Panstwa = {}
        for panstwo in DANE.daj_zaznaczone().daj_panstwa():
            nazwa = panstwo.daj_nazwa()
            ilosci = panstwo.daj_ilosc()
            dlugosc = len(ilosci)  # Pobranie długości listy ilości aut
            categories = [x + 2013 for x in range(dlugosc)]
            self.__Panstwa[nazwa] = [ilosci, categories]

        # Usuń poprzednie dane
        self.ax.clear()

        # Liczba serii danych
        num_series = len(self.__Panstwa)

        # Szerokość pojedynczego słupka
        bar_width = 0.35

        # Przesunięcie dla każdej serii danych
        bar_offsets = [-0.5 * bar_width + i * bar_width for i in range(num_series)]

        # Dodaj nowe dane
        for i, (label, (values, categories)) in enumerate(self.__Panstwa.items()):
            self.ax.bar([x + bar_offsets[i] for x in categories], values, label=label, width=bar_width)

        # Ustaw legendę
        self.ax.legend()

        # Odśwież wykres
        self.canvas.draw()
