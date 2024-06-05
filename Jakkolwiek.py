from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTabWidget

class OldButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__("Stwórz przycisk", parent)
        self.clicked.connect(self.create_button)

    def create_button(self):
        new_button = QPushButton("Stary przycisk")
        self.parent().layout().addWidget(new_button)

class NewButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__("Nowy przycisk", parent)
        self.clicked.connect(self.create_button)

    def create_button(self):
        new_button = QPushButton("Nowy przycisk")
        self.parent().layout().addWidget(new_button)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Przycisk tworzący przycisk")
        self.setGeometry(100, 100, 400, 300)

        # Tworzenie zakładek
        self.tab_widget = QTabWidget()

        # Zakładka 1 z przyciskami klasy OldButton
        self.tab1 = QWidget()
        layout_tab1 = QVBoxLayout()
        self.button_create_tab1 = OldButton(self.tab1)
        layout_tab1.addWidget(self.button_create_tab1)
        self.tab1.setLayout(layout_tab1)
        self.tab_widget.addTab(self.tab1, "Zakładka 1")

        # Zakładka 2 z przyciskami klasy NewButton
        self.tab2 = QWidget()
        layout_tab2 = QVBoxLayout()
        self.button_create_tab2 = NewButton(self.tab2)
        layout_tab2.addWidget(self.button_create_tab2)
        self.tab2.setLayout(layout_tab2)
        self.tab_widget.addTab(self.tab2, "Zakładka 2")

        # Ustawienie centralnego widgetu
        self.setCentralWidget(self.tab_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
