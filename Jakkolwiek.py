from PanstwaM import Panstwo, Lista_panstw, Lista_panstw_z_filtowaniem
Poland = Panstwo("Polska", [1,2,3])
Germany = Panstwo("Germany", [4,3,2])
Russia = Panstwo("Russia", [6,1,2])
Prime = Lista_panstw([Poland, Germany, Russia])
Filtr = Lista_panstw_z_filtowaniem([Poland, Germany, Russia])
print(Prime.daj_panstwa())
print(Filtr.daj_panstwa())
Filtr.filtruj("ge", Prime.daj_panstwa())
print(Filtr.daj_panstwa())
print(Prime.daj_panstwa())