class Panstwo(): #reprezentcja pojedynczego panstwa
    def __init__(self, nazwa, dane):
        self.__nazwa = nazwa
        self.__lista_ilosci_aut = dane

    def daj_nazwa(self):
        return self.__nazwa

    def daj_ilosc(self):
        return self.__lista_ilosci_aut

    def __repr__(self):
        return f"{self.__nazwa}"

    def __eq__(self, other):
        if isinstance(other, Panstwo):
            return self.__nazwa == other.__nazwa
        return False

class Lista_panstw(): #Bedzie robić za panstwa original i panstwa-
    def __init__(self, lista_obiektow_panstwo = []):
        self.__tablica_panstw = lista_obiektow_panstwo

    def daj_panstwa(self):
        return self.__tablica_panstw

    def dodaj_panstwo(self, panstwo):
        self.__tablica_panstw.append(panstwo)

    def usun_panstwo(self, panstwo):
        self.__tablica_panstw.remove(panstwo)

    def zeruj_liste(self):
        self.__tablica_panstw = []


class Lista_panstw_z_filtowaniem(Lista_panstw): #ma opcje filtowania
    def __init__(self, lista_obiektow_panstwo=[]):
        super().__init__(lista_obiektow_panstwo)

    def filtruj_liste(self, klucz, lista_filtorwana): #tutaj dostarczamy czystą listę poprzez Lista_panstw.daj_panstwa()
        self.zeruj_liste()
        klucz_lower = klucz.lower()
        for panstwo in lista_filtorwana:
            if klucz_lower in panstwo.daj_nazwa().lower():
                self.dodaj_panstwo(panstwo)
