from PyQt6.QtWidgets import QApplication
import sys
from Buttons_wspolne import MainWindow
from Dane_IO import Dane_porownywarka
from LadowarkiM import Lista_ladowarek


def main():
    DANE_1 = Dane_porownywarka()  # dane wykorzystywane w trybie rysowania wykresów
    DANE_2 = Lista_ladowarek()
    app = QApplication(sys.argv)
    window = MainWindow(DANE_1, DANE_2)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
