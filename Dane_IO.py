from abc import ABC, abstractmethod
import pandas as pd
from PanstwaM import Panstwo, Panstwaoriginal

class Wejscie(ABC):
    @abstractmethod
    def czytaj(self):
        pass

class xlsx_czytaj_wykres(Wejscie):
    def czytaj(self, path):
        wynik = self.__xlsx_do_pandas(path)
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
        panstwa = tabela.iloc[:, 0].tolist()
        dane_panstw = [row[1:].tolist() for row in tabela.values]
        return panstwa, dane_panstw

    def __stworz_obiekty(self, nazwy_panstw, dane_panstw):
        lista_obiektow_panstwo = []
        for index in range(len(nazwy_panstw)):
            temp = Panstwo(nazwy_panstw[index], dane_panstw[index])
            lista_obiektow_panstwo.append(temp)
        return Panstwaoriginal(lista_obiektow_panstwo)

