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
        arkusz = pd.read_excel(patch, sheet_name='Sheet 1')
