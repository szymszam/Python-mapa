import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ustawienia głównego okna
        self.setWindowTitle("Przykład Wykresu w PyQt6")
        self.setGeometry(100, 100, 800, 600)

        # Tworzenie QWidget jako centralnego widgetu
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Tworzenie layoutu
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Tworzenie wykresu Matplotlib
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Dodanie przykładowych danych do wykresu
        self.plot()

    def plot(self):
        x = [0, 1, 2, 3, 4, 5]
        y = [0, 1, 4, 9, 16, 25]
        self.ax.plot(x, y)
        self.ax.set_title("Przykładowy Wykres")
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
