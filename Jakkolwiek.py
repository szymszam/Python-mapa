import sys
import PyQt6.QtWidgets as qtw


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #tytuł
        self.setWindowTitle('Okno życia')

        #Ustawienie okna
        self.setLayout(qtw.QVBoxLayout())

        #Stwórz Label
        my_label = qtw.QLabel("Google")
        my_label.setFont(qtg.QFont('Times New Roman', 18))
        self.layout().addWidget(my_label)

        #Entry box
        my_entry = qtw.QLineEdit()
        #my_entry.setObjectName("nazwa")
        #my_entry.setText("Wyszukaj")
        self.layout().addWidget(my_entry)

        #Przycisk
        my_button = qtw.QPushButton("Szukaj",
                                clicked = lambda: klik())
        self.layout().addWidget(my_button)


        #Pokaz co stworzyłeś
        self.show()

        def klik():
            #Zmien label
            my_label.setText(my_entry.text())

            #zmien zawartość boxa
            my_entry.setText("")

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()