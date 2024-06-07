class szymon():
    def __init__(self,w):
        self.w = w
class olek():
    def __init__(self,slowo):
        self.slowo = slowo
    def metoda_create(self):
      return szymon(self)
    def drukuj(self):
      print(self.slowo)

olek = olek("slowo1")
szymon = olek.metoda_create()

szymon.w.drukuj()
olek.slowo ="beka"
szymon.w.drukuj()