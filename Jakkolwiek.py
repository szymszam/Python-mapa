from PanstwaM import Panstwa_filtrowane, Panstwa_zaznaczone, Panstwa_original, Panstwo
poland = Panstwo('Polska', [2, 3, 4])
germany = Panstwo('Niemcy', [2,4,1])
russia = Panstwo('Rosja', [5,2,1])

lista_original = [poland, germany, russia]
original = Panstwa_original(lista_original)
filtrowane = Panstwa_filtrowane(lista_original)
print(original.daj_panstwa())
print(filtrowane.daj_panstwa())
filtrowane.filtruj("a", lista_original)
print(filtrowane.daj_panstwa())