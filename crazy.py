from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])

main_win = QWidget()
mein_win.setWindowTitle("Визначник переможця")
mein_win.resize(400, 250)

text = QLabel("Натисніть щоб побачити переможця")
result = QLabel("?")
btn = QPushButton("Згенерувати")

line = QVBoxLayout()
line.add_Widget(text)
line.add_Widget(result)
line.add_Widget(btn)

main_win.setLayout(line)
main_win.show()

app.exec_()