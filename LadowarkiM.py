class Ladowarka:
    def __init__(self, x, y, nazwa):
        self.__x = x
        self.__y = y
        self.__nazwa = nazwa

    def daj_lokacje(self):
        return self.__x, self.__y

    def daj_nazwa(self):
        return self.__nazwa

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y


class Lista_ladowarek:
    def __init__(self, ladowarki):
        self.__ladowarki = ladowarki

    def daj_ladowarki(self):
        return self.__ladowarki

    def dodaj_ladowarke(self, ladowarka):
        self.__ladowarki.append(ladowarka)

    def usun_ladowarke(self, ladowarka):
        self.__ladowarki.remove(ladowarka)

