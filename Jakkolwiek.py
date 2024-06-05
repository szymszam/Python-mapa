import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 100, 600, 400)
        self.setWindowTitle('Przycisk Tworzący Przycisk')

        self.init_view()
        self.show()

    def init_view(self):
        # Tworzenie głównego widgetu
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Tworzenie głównego layoutu
        self.main_layout = QVBoxLayout()
        main_widget.setLayout(self.main_layout)

        # Tworzenie przycisku tworzącego nowe przyciski
        self.create_button = QPushButton('Stwórz nowy przycisk')
        self.create_button.clicked.connect(self.create_new_button)
        self.main_layout.addWidget(self.create_button)

    def create_new_button(self):
        # Tworzenie nowego przycisku
        new_button = QPushButton('Nowy przycisk')
        new_button.clicked.connect(lambda: print('Kliknięto nowy przycisk'))
        self.main_layout.addWidget(new_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())