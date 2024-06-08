import sys
from PyQt6 import QtWidgets


class Obsluga_mapy(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Layouty poziome dla pól tekstowych i przycisków
        text_layout = QtWidgets.QHBoxLayout()
        button_layout = QtWidgets.QHBoxLayout()

        # Tworzenie pól tekstowych
        self.pole_x = QtWidgets.QLineEdit(self)
        self.pole_x.setPlaceholderText("Podaj X")
        self.pole_y = QtWidgets.QLineEdit(self)
        self.pole_y.setPlaceholderText("Podaj Y")
        self.pole_nazwa = QtWidgets.QLineEdit(self)
        self.pole_nazwa.setPlaceholderText("Podaj Nawa")

        # Dodanie pól tekstowych do layoutu
        text_layout.addWidget(self.pole_x)
        text_layout.addWidget(self.pole_y)
        text_layout.addWidget(self.pole_nazwa)

        # Tworzenie przycisków
        self.Dodawanie = QtWidgets.QPushButton('Dodaj stacje', self)
        self.Dodawanie.clicked.connect(self.Dodaj_stacje)
        self.Usuwanie = QtWidgets.QPushButton('Usun stacje', self)
        self.Usuwanie.clicked.connect(self.Usun_stacje)

        # Dodanie przycisków do layoutu
        button_layout.addWidget(self.Dodawanie)
        button_layout.addWidget(self.Usuwanie)

        # Główny layout
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(text_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def Dodaj_stacje(self):
        print("Dodaje")

    def Usun_stacje(self):
        print("spijasz")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = Obsluga_mapy()
    window.setWindowTitle("Obsługa Mapy")
    window.setGeometry(100, 100, 600, 200)
    window.show()

    sys.exit(app.exec())

