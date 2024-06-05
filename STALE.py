from PanstwaM import Panstwo, Lista_panstw

class Dane:
    def __init__(self):
        self.__panstwa_orginalne = 0
        self.__panstwa_zaznaczone = 0
        self.__panstwa_filtrowane = 0

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


DANE = Dane()
polska = Panstwo("Polska", [1, 2, 4])
niemcy = Panstwo("Niemcy", [1, 3, 4])
lista = Lista_panstw([polska, niemcy])
DANE.zamien_orginalne(lista)
DANE.zamien_filtrowane(lista)


#plik_z_danymi = "C:\\Users\\User\\Desktop\\road_eqr_carpda_spreadsheet.xlsx"


plik_z_danymi = r"C:\Users\olech\Desktop\road_eqr_carpda_spreadsheet.xlsx"