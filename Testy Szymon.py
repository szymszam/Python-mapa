from Dane_IO import Fabryka_wejscia, Wejscie_xlsx
from PanstwaM import Panstwo, Lista_panstw
from STALE import plik_z_danymi

czytajnik = Fabryka_wejscia()
czytaj_xlsx = czytajnik.daj_wejscie(plik_z_danymi)
lista = czytaj_xlsx.czytaj()

print(lista)

lista = lista.daj_panstwa()



for i in range(len(lista)):
    print(lista[i].daj_nazwa())
#masz <3

