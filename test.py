from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QRadioButton,QHBoxLayout, QMessageBox, QPushButton, QLabel, QVBoxLayout

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle("Конкурс від Crazy People")
main_win.resize(400, 200)

question = QLabel("В якому році канал отримав 'золоту кнопку' від YouTube?")
btn1 = QRadioButton("2005")
btn2 = QRadioButton("2010")
btn3 = QRadioButton("2015")  
btn4 = QRadioButton("2020")    

vline = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()

vline.addWidget(question, alignment=Qt.AlignCenter) 
row1.addWidget(btn1,alignment=Qt.AlignCenter)
row1.addWidget(btn2,alignment=Qt.AlignCenter)
row2.addWidget(btn3,alignment=Qt.AlignCenter)
row2.addWidget(btn4,alignment=Qt.AlignCenter)

vline.addLayout(row1)
vline.addLayout(row2)


main_win.setLayout(vline)

def show_win():
    message = QMessageBox()
    message.setText("Ви вгадали!")
    message.exec_()

btn3.clicked.connect(show_win)



main_win.show()
app.exec_()

