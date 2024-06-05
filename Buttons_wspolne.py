from PyQt6.QtWidgets import QTabWidget, QPushButton, QVBoxLayout, QWidget, QMainWindow
from Dane_IO import Fabryka_wejscia
from Buttons_porownywarka import Buttons_lista_panstw, Searchbar
from STALE import plik_z_danymi, DANE

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 100, 1300, 900)
        self.setWindowTitle('Los Elektrikos')

        self.__init_view()
        self.show()

    def __init_view(self):
        buttons_trybow_panel = Buttons_trybow_panel()

        # Tworzenie głównego widgetu
        main_widget = QWidget(self)
        main_layout = QVBoxLayout()
        main_layout.addWidget(buttons_trybow_panel)
        main_widget.setLayout(main_layout)

        # Ustawienie głównego widgetu jako centralny widget
        self.setCentralWidget(main_widget)

class Buttons_trybow_panel(QTabWidget):
    def __init__(self):
        super().__init__()
        self.stworz_tab1()
        self.stworz_tab2()
        self.stworz_tab3()
        self.stworz_taby()

    def stworz_tab1(self):
        # Tworzenie widgetu dla pierwszej zakładki
        self.tab1 = QWidget()
        self.tab1_layout = QVBoxLayout()

        self.tab1_layout.addWidget(Button_Wczytywanie(parent_panel=self))
        self.tab1.setLayout(self.tab1_layout)

    def stworz_tab2(self):
        # Tworzenie widgetu dla drugiej zakładki
        self.tab2 = QWidget()
        self.tab2_layout = QVBoxLayout()
        self.tab2_layout.addWidget(Searchbar())
        self.tab2.setLayout(self.tab2_layout)

    def wyczysc_tab2(self):
        for i in reversed(range(self.tab2_layout.count())):
            widget_to_remove = self.tab2_layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.setParent(None)

    def umebluj_tab2(self):
        self.wyczysc_tab2()
        self.tab2_layout.addWidget(Buttons_lista_panstw())

    def stworz_tab3(self):
        self.tab3 = QWidget()
        self.tab3_layout = QVBoxLayout()
        self.tab3.setLayout(self.tab3_layout)

    def stworz_taby(self):
        # Dodawanie zakładek do widgetu
        self.addTab(self.tab1, "Wczytywanie")
        self.addTab(self.tab2, "Porownywarka")
        self.addTab(self.tab3, "Mapa")

class Button_Wczytywanie(QPushButton):
    def __init__(self, parent_panel):
        super().__init__("Wczytywanie", parent_panel)
        self.parent_panel = parent_panel
        self.clicked.connect(self.__klik)

    def __klik(self):
        #wczytwanie danych
        czytajnik = Fabryka_wejscia()
        czytajnik = czytajnik.daj_wejscie(plik_z_danymi)
        dane = czytajnik.czytaj()
        global DANE
        DANE.zamien_orginalne(dane)
        DANE.zamien_filtrowane(dane)

        # Wywołanie metod z klasy Buttons_trybow_panel
        self.parent_panel.stworz_tab2()
        self.parent_panel.wyczysc_tab2()

        #Kasowanie zakładki całej
        index = self.parent_panel.indexOf(self.parent_panel.tab1)
        self.parent_panel.removeTab(index)
