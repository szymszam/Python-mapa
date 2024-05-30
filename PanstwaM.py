class panstwo():
    def __init__(self, nazwa, dane):
        self.__nazwa = nazwa
        self.__lista_ilosci_aut = dane

    def daj_nazwa(self):
        return self.__nazwa

    def daj_ilosc(self):
        return self.__lista_ilosci_aut

    def __repr__(self):
        return f"panstwo(nazwa={self.__nazwa}, dane={self.__lista_ilosci_aut})"


class panstwaoriginal():
    def __init__(self, lista_obiektow_panstw):
        self.__panstwa = lista_obiektow_panstw

    def daj_panstwa(self):
        return self.__panstwa