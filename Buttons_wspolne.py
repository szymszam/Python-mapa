from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTabWidget, QPushButton, QVBoxLayout, QWidget, QMainWindow, QGridLayout, QFileDialog
from PyQt6.QtGui import QFont
from Dane_IO import Fabryka_wejscia_wykresy
from Buttons_porownywarka import Buttons_lista_panstw, Szukaj_i_zapisz, Suwaki_lat
from PanstwaM import Lista_panstw_z_filtowaniem
from Wykres_porownywarka import Wykres


class MainWindow(QMainWindow):
    def __init__(self, DANE_1):
        super().__init__()
        self.__DANE_1 = DANE_1
        self.setWindowTitle('Los Elektrikos')

        self.__init_view()
        self.showFullScreen()  # Maksymalizuj okno po jego utworzeniu

    def __init_view(self):
        self.buttons_trybow_panel = Buttons_trybow_panel(self, self.__DANE_1)

        # Tworzenie głównego widgetu
        main_widget = QWidget(self)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.buttons_trybow_panel)
        main_widget.setLayout(main_layout)

        # Ustawienie głównego widgetu jako centralny widget
        self.setCentralWidget(main_widget)


class Buttons_trybow_panel(QTabWidget):
    def __init__(self, main_window, DANE_1):
        super().__init__()

        self.main_window = main_window

        self.__DANE_1 = DANE_1

        # Tworzenie i dodawanie zakładek
        self.tab1 = Tab1(self, self.__DANE_1)
        self.addTab(self.tab1, "Wczytywanie")

    def stworz_tab2(self):
        self.tab2 = Tab2(self, self.__DANE_1)
        self.addTab(self.tab2, "Porownywarka")

    def stworz_tab3(self):
        self.tab3 = Tab3(self)
        self.addTab(self.tab3, "Mapa")

    def wyczysc_tab2(self):
        self.tab2.wyczysc_tab2()

    def zapelnij_bts_panstwa_tab2(self):
        self.tab2.zapelnij_bts_panstwa_tab2()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            if self.isFullScreen():
                self.showNormal()  # Wyjście z trybu pełnoekranowego
            self.close()


class Tab1(QWidget):
    def __init__(self, parent, DANE_1):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        button = Button_Wczytywanie(parent, DANE_1)
        button.setParent(self)
        button.move(750, 360)



class Tab2(QWidget):
    def __init__(self, parent, DANE_1):
        super().__init__(parent)
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)
        self.__DANE_1 = DANE_1

        self.__Wykres = Wykres(self.__DANE_1)
        self.__Reszta_przyciskow = Szukaj_i_zapisz(self, self.__DANE_1, self.__Wykres)
        self.__Suwaki = Suwaki_lat(self.__DANE_1, self.__Wykres)

        self.__Wykres.setParent(self)
        self.__Reszta_przyciskow.setParent(self)
        self.__Suwaki.setParent(self)

        self.__Wykres.move(0, 0)
        self.__Wykres.setFixedSize(1300, 900)

        self.__Reszta_przyciskow.move(1300, 50)
        self.__Reszta_przyciskow.setFixedSize(400, 50)

        self.__Suwaki.move(200,900)
        self.__Suwaki.setFixedSize(700, 150)


    def wyczysc_tab2(self):
        self.__Przyciski_panstw.setVisible(False)



    def zapelnij_bts_panstwa_tab2(self):
         self.__Przyciski_panstw = Buttons_lista_panstw(self.__Wykres, self.__DANE_1)
         self.__Przyciski_panstw.setParent(self)
         self.__Przyciski_panstw.move(1300, 100)
         self.__Przyciski_panstw.setFixedSize(400, 800)
         self.__Przyciski_panstw.setVisible(True)


class Tab3(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QGridLayout(self)
        self.setLayout(self.layout)

        # Dodanie widgetów do layoutu, jeśli jakieś są potrzebne
        # self.layout.addWidget(...)


class Button_Wczytywanie(QPushButton):
    def __init__(self, glowny_panel, DANE_1):
        super().__init__("Wczytywanie")
        self.__glowny_panel = glowny_panel
        self.__DANE_1 = DANE_1

        self.setFixedSize(400, 120)
        font = QFont("Arial", 26)
        self.setFont(font)

        self.clicked.connect(self.klik)
        self.setFixedSize(400, 100)
        self.setStyleSheet("font-size: 24px; font-family: Arial")

    def klik(self):
        # Wybór pliku za pomocą dialogu
        plik, _ = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "Wszystkie pliki (*)")

        if plik:
            # Wczytywanie danych do DANE
            czytajnik = Fabryka_wejscia_wykresy()
            czytajnik = czytajnik.daj_wejscie(plik)
            dane_zczytane = czytajnik.czytaj()
            self.__DANE_1.zamien_orginalne(dane_zczytane)
            dane_zczytane = dane_zczytane.daj_panstwa()
            self.__DANE_1.zamien_filtrowane(Lista_panstw_z_filtowaniem(dane_zczytane))

            # Zmiana tekstu przycisku na "Dane zostały wczytane"
            self.setText("Dane zostały wczytane")

            # Blokowanie przycisku po naciśnięciu
            self.setDisabled(True)

            # Tworzenie zakładek 2 i 3 i zapełnienie zakładki 2
            self.__glowny_panel.stworz_tab2()
            self.__glowny_panel.stworz_tab3()
            self.__glowny_panel.zapelnij_bts_panstwa_tab2()

            self.__DANE_1.zmien_ost_rok(len(self.__DANE_1.daj_orginalne().daj_panstwa()[0].daj_ilosc()))
