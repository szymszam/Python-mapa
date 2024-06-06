from PyQt6.QtWidgets import  QApplication
import sys
from Buttons_wspolne import MainWindow
from Dane_IO import Dane_porownywarka

def main():
    DANE_1 = Dane_porownywarka() #dane wykorzystywane w trybie rysowania wykresów
    app = QApplication(sys.argv)
    window = MainWindow(DANE_1)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()