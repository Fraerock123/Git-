import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QColor
from PyQt6.uic import loadUi


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI.ui', self)
        self.button = self.findChild(QPushButton, 'pushButton')
        self.button.clicked.connect(self.draw_circle)
        self.circles = []

    def draw_circle(self):
        x = random.randint(50, self.width() - 50)
        y = random.randint(50, self.height() - 50)
        diameter = random.randint(20, 100)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(255, 255, 0))
        for x, y, diameter in self.circles:
            painter.drawEllipse(QPoint(x, y), diameter // 2, diameter // 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())