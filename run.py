from PyQt6.QtWidgets import  QApplication
import sys
from Buttons_wspolne import MainWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()