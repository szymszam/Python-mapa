from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class wykres(FigureCanvasQTAgg):
    def __init__(self, width=5, height=4, dpi=100):
        self.__fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.__fig)

    def dodaj_nowy_wykres(self, name, color):
        if self.__axes is None:
            self.__axes = self.__fig.add_subplot(111)

        x_start, x_end = 2015, 2024 # tutaj jest zakres lat
        xx = range(x_start, x_end)
        yy= [23, 45, 56, 78, 89, 1, 2, 3, 5, 12]
        self.__axes.plot(xx, yy, color=color)
        self.__axes.legend()
        self.draw()


class lata():
    def __init__(self):
        pass

