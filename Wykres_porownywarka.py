import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFileDialog
import seaborn as sns

class Wykres(QWidget):
    def __init__(self, DANE_1):
        super().__init__()
        self.__DANE_1 = DANE_1

        # Ustaw styl wykresu
        sns.set(style="whitegrid")

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
        self.ax.set_title("Wykres", fontsize=16)
        self.ax.set_xlabel("Lata", fontsize=14)
        self.ax.set_ylabel("Liczba aut", fontsize=14)

        # Inicjalizuj dane
        self.__Panstwa = []  # Słownik przechowujący serie danych {label: (categories, values)}

        # Dodaj przykładowe dane do wykresu
        self.zaladuj_wykres()

#Aktualizacja wykresu - wykorzusyje dane zawarte w DANE_1 a dokładniej panstwa zazanaczone oraz lata
    def zaladuj_wykres(self):
        self.__Panstwa = []
        for panstwo in self.__DANE_1.daj_zaznaczone().daj_panstwa():
            nazwa = panstwo.daj_nazwa()
            ilosci = panstwo.daj_ilosc()
            categories = [x + 2013 for x in range(len(ilosci) )]
            self.__Panstwa.append([nazwa, ilosci[self.__DANE_1.daj_pier_rok():self.__DANE_1.daj_ost_rok()], categories[self.__DANE_1.daj_pier_rok():self.__DANE_1.daj_ost_rok()]])

        # Usuń poprzednie dane
        self.ax.clear()

        # Liczba serii danych
        num_series = len(self.__Panstwa)

        # Szerokość pojedynczego słupka
        bar_width = 0.35

        # Przesunięcie dla każdej serii danych
        bar_offsets = [-0.5 * bar_width + i * bar_width for i in range(num_series)]

        # Kolory słupków
        colors = sns.color_palette("husl", num_series)

        # Dodaj nowe dane
        for i, (nazwa, ilosci, categories) in enumerate(self.__Panstwa):
            bars = self.ax.bar([x + bar_offsets[i] for x in categories], ilosci, label=nazwa, width=bar_width, color=colors[i])
            # Dodaj etykiety na słupkach
            for bar in bars:
                yval = bar.get_height()
                self.ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, int(yval), ha='center', va='bottom')

        # Ustaw tytuł wykresu
        self.ax.set_title("Liczba rejestracji pojazdów elektrycznych", fontsize=16)

        # Ustaw etykiety osi X
        all_years = []
        for _, _, categories in self.__Panstwa:
            all_years.extend(categories)
        unique_years = sorted(set(all_years))
        self.ax.set_xticks(unique_years)
        self.ax.set_xticklabels(unique_years, rotation=45)

        # Ustaw siatkę
        self.ax.grid(True, which='both', linestyle='--', linewidth=0.5)

        # Ustaw legendę
        self.ax.legend(title="Państwa")

        # Odśwież wykres
        self.canvas.draw()

    def zapisz_wykres_jako_pdf(self):
        nazwa_pliku, _ = QFileDialog.getSaveFileName(self, "Zapisz jako", "", "Pliki PDF (*.pdf)")

        if nazwa_pliku:
            self.figure.savefig(nazwa_pliku, format='pdf')
