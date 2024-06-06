from PanstwaM import  Lista_panstw, Lista_panstw_z_filtowaniem
class Dane:
    def __init__(self):
        self.__panstwa_orginalne = Lista_panstw()
        self.__panstwa_zaznaczone = Lista_panstw()
        self.__panstwa_filtrowane = Lista_panstw_z_filtowaniem()

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
