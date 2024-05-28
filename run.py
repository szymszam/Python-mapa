from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QVBoxLayout
import sys
from Widok_porownywarka import wykres
from Buttons_wspolne import Buttons_trybow_panel


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(350, 100, 1300, 900)
        self.setWindowTitle('Los Elektrikos')

        self.__init_view()
        self.show()

    def __init_view(self):
        porownywarka = wykres()
        buttons_trybow_panel = Buttons_trybow_panel()

        main_layout = QVBoxLayout()
        # main_layout.addWidget(porownywarka, 0, 0)
        main_layout.addWidget(buttons_trybow_panel)

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
