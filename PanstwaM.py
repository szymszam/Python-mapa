class Panstwo():
    def __init__(self, nazwa, dane):
        self.__nazwa = nazwa
        self.__lista_ilosci_aut = dane

    def daj_nazwa(self):
        return self.__nazwa

    def daj_ilosc(self):
        return self.__lista_ilosci_aut

    def __repr__(self):
        return f"panstwo(nazwa={self.__nazwa}, dane={self.__lista_ilosci_aut})"

    def __eq__(self, other):
        if isinstance(other, Panstwo):
            return self.__nazwa == other.__nazwa
        return False


class Panstwa_original():
    def __init__(self, lista_obiektow_panstwo):
        self.__tablica_panstw = lista_obiektow_panstwo

    def daj_panstwa(self):
        return self.__tablica_panstw

class Panstwa_zaznaczone(Panstwa_original):
    def __init__(self):
        self.__tablica_panstw = []

    def dodaj_panstwo(self, panstwo):
        self.__tablica_panstw.append(panstwo)

    def usun_panstwo(self, panstwo):
        self.__tablica_panstw.remove(panstwo)

class Panstwa_filtrowane():
    def __init__(self, lista_obiektow_panstwo):
        self.__tablica_panstw = lista_obiektow_panstwo

    def daj_panstwa(self):
        return self.__tablica_panstw

    def filtruj(self, klucz, lista_pierwotna):
        self.__tablica_panstw = []
        for panstwo in lista_pierwotna:
            if klucz in panstwo.daj_nazwa():
                self.__tablica_panstw.append(panstwo)