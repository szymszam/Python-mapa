from abc import ABC, abstractmethod
import pandas as pd

class Wejscie(ABC):
    @abstractmethod
    def czytaj(self):
        pass

class xlsx_czytaj_wykres(Wejscie):
    def czytaj(self):
        pass

    def xlsx_do_pandas(self, patch):
        arkusz_wycinek = pd.read_excel(patch, sheet_name='Sheet 1')
        arkusz_wycinek = arkusz_wycinek.iloc[9:]
        arkusz_wycinek = arkusz_wycinek.reset_index(drop=True)
        indeks_konca = arkusz_wycinek[arkusz_wycinek.eq("Special value").any(axis=1)].index[0] - 1
        arkusz_wycinek = arkusz_wycinek.iloc[:indeks_konca]
        return arkusz_wycinek

    def kondycjonuj(self, tabela):
        tabela = tabela.drop(tabela.columns[2::2], axis=1)
        tabela = tabela.replace(':', 0)
        panstwa = tabela.iloc[:, 0].tolist()
        dane_panstw = [row[1:].tolist() for row in tabela.values]
        print(panstwa[0])
        print(dane_panstw[0])


test = xlsx_czytaj_wykres()
test.kondycjonuj(test.xlsx_do_pandas("C:\\Users\\User\\Desktop\\road_eqr_carpda_spreadsheet.xlsx"))