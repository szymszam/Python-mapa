from PyQt6.QtWidgets import QTabWidget, QPushButton, QVBoxLayout, QWidget, QMainWindow, QGridLayout
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
    # Gdy powstaje obiekt to powstaje tylko jedna zakładka automatycznie reszte trzeba metodami
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.stworz_tab1()

    def stworz_tab1(self):
        # Tworzenie widgetu dla pierwszej zakładki
        self.tab1 = QWidget()
        self.tab1_layout = QVBoxLayout()
        self.tab1.setLayout(self.tab1_layout)

        self.tab1_layout.addWidget(Button_Wczytywanie(self))

        self.addTab(self.tab1, "Wczytywanie")

    def stworz_tab2(self):
        # Tworzenie widgetu dla drugiej zakładki
        self.tab2 = QWidget()
        self.tab2_layout = QGridLayout()
        self.tab2.setLayout(self.tab2_layout)

        self.__Searchbar = Searchbar(self)
        self.__Wykres = Wykres()

        self.tab2_layout.addWidget(self.__Searchbar, 0, 1)
        self.tab2_layout.addWidget(self.__Wykres, 1, 0)

        self.addTab(self.tab2, "Porownywarka")

    # czysci przyciski panstw z tab2
    def wyczysc_tab2(self):
        for i in reversed(range(self.tab2_layout.count())):
            widget_to_remove = self.tab2_layout.itemAt(i).widget()
            if isinstance(widget_to_remove, Buttons_lista_panstw):
                widget_to_remove.setParent(None)

    # zapełnia tab 2 searchbarem guzikiem i gizikami panstw
    def zapelnij_tab2(self):
        self.tab2_layout.addWidget(Buttons_lista_panstw(self.__Wykres), 1, 1)

    def stworz_tab3(self):
        # Tworzenie widgetu dla trzeciej zakładki
        self.tab3 = QWidget()
        self.tab3_layout = QGridLayout()
        self.tab3.setLayout(self.tab3_layout)

        self.addTab(self.tab3, "Mapa")


class Button_Wczytywanie(QPushButton):
    def __init__(self, glowny_panel):
        super().__init__("Wczytywanie")
        self.__glowny_panel = glowny_panel
        self.clicked.connect(self.klik)

    def klik(self):
        # Wczytywanie danych do DANE
        czytajnik = Fabryka_wejscia()
        czytajnik = czytajnik.daj_wejscie(plik_z_danymi)
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
        self.__glowny_panel.zapelnij_tab2()
