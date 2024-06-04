from Dane_IO import Fabryka_wejscia, Wejscie_xlsx
from PanstwaM import Panstwo, Lista_panstw

czytajnik = Fabryka_wejscia()
czytaj_xlsx = czytajnik.daj_wejscie(r"C:\Users\User\Desktop\road_eqr_carpda_spreadsheet.xlsx")
lista = czytaj_xlsx.czytaj()
lista = lista.daj_panstwa()
print(lista[0].daj_nazwa())
#masz <3
