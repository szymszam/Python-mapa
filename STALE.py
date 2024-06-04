plik_z_danymi = "C:\\Users\\User\\Desktop\\road_eqr_carpda_spreadsheet.xlsx"

class Dane:
    def __init__(self):
        self.__panstwa_orginalne = []
        self.__panstwa_zaznaczone = []
        self.__panstwa_filtrowane = []

    def daj_orginalne(self):
        return self.__panstwa_orginalne

    def daj_zaznaczone(self):
        return self.__panstwa_zaznaczone

    def daj_filtrowane(self):
        return self.__panstwa_filtrowane

    def zamien_orginalne(self, nowa_lista):
        self.__panstwa_orginalne = nowa_lista

    def zamien_zaznaczone(self, nowa_lista):
        self.__panstwa_zaznaczone = nowa_lista

    def zamien_filtrowane(self, nowa_lista):
        self.__panstwa_filtrowane = nowa_lista