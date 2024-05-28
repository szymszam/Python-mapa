from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout
import sys
from Widok_porownywarka import wykres


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(350, 100, 1300, 900)
        self.setWindowTitle('Los Elektrikos')

        self.__init_view()
        self.show()

    def __init_view(self):
        porownywarka = wykres()

        main_layout = QGridLayout()
        main_layout.addWidget(porownywarka, 0, 0)

        main_widget = QWidget(self)
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
