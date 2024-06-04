from Dane_IO import Fabryka_wejscia, Wejscie_xlsx
from PanstwaM import Panstwo, Lista_panstw

czytajnik = Fabryka_wejscia()
czytaj_xlsx = czytajnik.daj_wejscie(r"C:\Users\olech\Desktop\road_eqr_carpda_spreadsheet.xlsx")#r"C:\Users\User\Desktop\road_eqr_carpda_spreadsheet.xlsx"
lista = czytaj_xlsx.czytaj()

print(lista)

lista = lista.daj_panstwa()



for i in range(len(lista)):
    print(lista[i].daj_nazwa())
#masz <3
