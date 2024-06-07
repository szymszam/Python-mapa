from abc import ABC, abstractmethod
import pandas as pd
from PanstwaM import Panstwo, Lista_panstw, Lista_panstw_z_filtowaniem

class Fabryka_wejscia_wykresy(): #wybiera i tworzy odpowiednie wejscie zczytujace
    def daj_wejscie(self, sciezka):
        rozszerzenie = sciezka.split(".")[-1]
        if rozszerzenie == "xlsx":
            return Wejscie_xlsx_wykresy(sciezka)
        else:
            raise ValueError("Nieobslugiwany typ pliku")

class Wejscie(ABC): #interface
    @abstractmethod
    def czytaj(self):
        pass

class Wejscie_xlsx_wykresy(Wejscie): #dajemy scierzke zwraca nam obiekt klasy Lista_panstw
    def __init__(self, sciezka):
        self.sciezka = sciezka

    def czytaj(self):
        wynik = self.__xlsx_do_pandas(self.sciezka)
        wynik = self.__kondycjonuj(wynik)
        wynik = self.__stworz_obiekty(wynik[0], wynik[1])
        return wynik

    def __xlsx_do_pandas(self, patch):
        arkusz_wycinek = pd.read_excel(patch, sheet_name='Sheet 1')
        arkusz_wycinek = arkusz_wycinek.iloc[9:]
        arkusz_wycinek = arkusz_wycinek.reset_index(drop=True)
        indeks_konca = arkusz_wycinek[arkusz_wycinek.eq("Special value").any(axis=1)].index[0] - 1
        arkusz_wycinek = arkusz_wycinek.iloc[:indeks_konca]
        return arkusz_wycinek

    def __kondycjonuj(self, tabela):
        tabela = tabela.drop(tabela.columns[2::2], axis=1)
        tabela = tabela.replace(':', 0)
        nazwy_panstw = tabela.iloc[:, 0].tolist()
        dane_panstw = [row[1:].tolist() for row in tabela.values]
        return nazwy_panstw, dane_panstw

    def __stworz_obiekty(self, nazwy_panstw, dane_panstw):
        lista_obiektow_panstwo = []
        for index in range(len(nazwy_panstw)):
            temp = Panstwo(nazwy_panstw[index], dane_panstw[index])
            lista_obiektow_panstwo.append(temp)
        return Lista_panstw(lista_obiektow_panstwo)

class Dane_porownywarka:
    def __init__(self):
        self.__panstwa_orginalne = Lista_panstw()
        self.__panstwa_zaznaczone = Lista_panstw()
        self.__panstwa_filtrowane = Lista_panstw_z_filtowaniem()
        self.__pier_rok_wyk = 6
        self.__ost_rok_wyk = 10


    def daj_orginalne(self):
        return self.__panstwa_orginalne

    def zamien_orginalne(self, nowa_lista):
        self.__panstwa_orginalne = nowa_lista


    def daj_zaznaczone(self):
        return self.__panstwa_zaznaczone

    def zamien_zaznaczone(self, nowa_lista):
        self.__panstwa_zaznaczone = nowa_lista


    def daj_filtrowane(self):
        return self.__panstwa_filtrowane

    def zamien_filtrowane(self, nowa_lista):
        self.__panstwa_filtrowane = nowa_lista




    def daj_pier_rok(self):
        return self.__pier_rok_wyk

    def zmien_pier_rok(self, nowy_rok):
        self.__pier_rok_wyk = nowy_rok

    def daj_ost_rok(self):
        return self.__ost_rok_wyk

    def zmien_ost_rok(self, nowy_rok):
        self.__ost_rok_wyk = nowy_rok

