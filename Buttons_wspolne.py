from abc import ABC, abstractmethod


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

    def set_position(self, x, y):
        self.__position = {"x": x, "y": y}

class Button_trybu_mapa(Button_trybu):
    def __init__(self):
        self.__mapa = {"x": 0, "y": 0}

    def set_position(self, x, y):
        self.__mapa = {"x": x, "y": y}

class Buttons_trybow_panel():
    pass
