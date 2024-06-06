from PyQt6.QtWidgets import QTabWidget, QPushButton, QVBoxLayout, QWidget, QMainWindow, QGridLayout, QFileDialog
from Dane_IO import Fabryka_wejscia
from Buttons_porownywarka import Buttons_lista_panstw, Searchbar
from STALE import plik_z_danymi, DANE
from PanstwaM import Lista_panstw_z_filtowaniem
from Widok_porownywarka import Wykres


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 100, 1500, 1100)
        self.setWindowTitle('Los Elektrikos')

        self.__init_view()
        self.show()

    def __init_view(self):
        self.buttons_trybow_panel = Buttons_trybow_panel(self)

        # Tworzenie głównego widgetu
        main_widget = QWidget(self)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.buttons_trybow_panel)
        main_widget.setLayout(main_layout)

        # Ustawienie głównego widgetu jako centralny widget
        self.setCentralWidget(main_widget)


class Buttons_trybow_panel(QTabWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # Tworzenie i dodawanie zakładek
        self.tab1 = Tab1(self)
        self.addTab(self.tab1, "Wczytywanie")

    def stworz_tab2(self):
        self.tab2 = Tab2(self)
        self.addTab(self.tab2, "Porownywarka")

    def stworz_tab3(self):
        self.tab3 = Tab3(self)
        self.addTab(self.tab3, "Mapa")

    def wyczysc_tab2(self):
        self.tab2.wyczysc_tab2()

    def zapelnij_bts_panstwa_tab2(self):
        self.tab2.zapelnij_bts_panstwa_tab2()


class Tab1(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.layout.addWidget(Button_Wczytywanie(parent))


class Tab2(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)

        self.__Searchbar = Searchbar(self)
        self.__Wykres = Wykres()

        self.layout.addWidget(self.__Searchbar, 0, 1)
        self.layout.addWidget(self.__Wykres, 1, 0)

    def wyczysc_tab2(self):
        for i in reversed(range(self.layout.count())):
            widget_to_remove = self.layout.itemAt(i).widget()
            if isinstance(widget_to_remove, Buttons_lista_panstw):
                widget_to_remove.setParent(None)

    def zapelnij_bts_panstwa_tab2(self):
        self.layout.addWidget(Buttons_lista_panstw(self.__Wykres), 1, 1)


class Tab3(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)

        # Dodanie widgetów do layoutu, jeśli jakieś są potrzebne
        # self.layout.addWidget(...)


class Button_Wczytywanie(QPushButton):
    def __init__(self, glowny_panel):
        super().__init__("Wczytywanie")
        self.__glowny_panel = glowny_panel
        self.clicked.connect(self.klik)

    def klik(self):
        # Wybór pliku za pomocą dialogu
        plik, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "Wszystkie pliki (*)")

        if plik:
            # Wczytywanie danych do DANE
            czytajnik = Fabryka_wejscia()
            czytajnik = czytajnik.daj_wejscie(plik)
            dane_zczytane = czytajnik.czytaj()
            DANE.zamien_orginalne(dane_zczytane)
            dane_zczytane = dane_zczytane.daj_panstwa()
            DANE.zamien_filtrowane(Lista_panstw_z_filtowaniem(dane_zczytane))

            # Usunięcie zakładki tab1 po wczytaniu danych
            index = self.__glowny_panel.indexOf(self.__glowny_panel.tab1)
            self.__glowny_panel.removeTab(index)

            # Tworzenie zakładek 2 i 3 i zapełnienie zakładki 2
            self.__glowny_panel.stworz_tab2()
            self.__glowny_panel.stworz_tab3()
            self.__glowny_panel.zapelnij_bts_panstwa_tab2()
