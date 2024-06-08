class Ladowarka:
    def __init__(self, x, y, nazwa):
        self.__x = x
        self.__y = y
        self.__nazwa = nazwa

    def daj_X(self):
        return self.__x

    def daj_Y(self):
        return self.__y

    def daj_nazwa(self):
        return self.__nazwa
    def __repr__(self):
        return f"Nazwa:{self.__nazwa} X:{self.__x} Y:{self.__y}"

    def __eq__(self, other):
        return self.__nazwa == other.__nazwa or self.__x == other.__x and self.__y == other.__y


class Lista_ladowarek:
    def __init__(self, ladowarki = []):
        self.__ladowarki = ladowarki

    def daj_ladowarki(self):
        return self.__ladowarki

    def dodaj_ladowarke(self, ladowarka):
        self.__ladowarki.append(ladowarka)

    def usun_ladowarke(self, ladowarka):
        self.__ladowarki.remove(ladowarka)

