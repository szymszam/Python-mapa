from abc import ABC, abstractmethod

from PyQt6.QtWidgets import QGroupBox, QHBoxLayout, QPushButton


class Button_trybu(ABC):
    @abstractmethod
    def klik(self):
        raise "spierdalaj"

    @abstractmethod
    def set_position(self, x, y):
        raise "brak zaznaczonego miejsca"


class Button_trybu_porownywarka(Button_trybu):
    def __init__(self):
        self.__position = {"x": 0, "y": 0}

    def klik(self):
        print("brak kodu")

    def set_position(self, x, y):
        self.__position = {"x": x, "y": y}


class Button_trybu_mapa(Button_trybu):
    def __init__(self):
        self.__mapa = {"x": 0, "y": 0}

    def klik(self):
        print("brak kodu")

    def set_position(self, x, y):
        self.__mapa = {"x": x, "y": y}


class Buttons_trybow_panel(QGroupBox):
    def __init__(self):
        super().__init__()

        # Tworzenie układu poziomego
        layout = QHBoxLayout()

        # Tworzenie przycisków
        button1 = QPushButton("Porownywarka")
        button1.clicked.connect(Button_trybu_porownywarka().klik)

        button2 = QPushButton("Mapa")
        button2.clicked.connect(Button_trybu_mapa().klik)

        # Dodawanie przycisków do układu
        layout.addWidget(button1)
        layout.addWidget(button2)

        # Ustawianie układu dla tego widgetu
        self.setLayout(layout)
