import sys

import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        a = random.randint(30, 400)
        qp.setBrush(QColor(255, 215, 0))
        qp.drawEllipse(30, 30, a, a)
        b = random.randint(30, 400)
        qp.setBrush(QColor(255, 215, 0))
        qp.drawEllipse(200, 30, b, b)
        c = random.randint(30, 400)
        qp.setBrush(QColor(255, 215, 0))
        qp.drawEllipse(400, 30, c, c)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
