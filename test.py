from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
import sys


SIZE = 3
WIN_COUNT = 3



class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        
        # self.initUI()
        
        self.board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
        
        # برای استفاده از الگوریتم minmax، باید به خط حرکت ها دسترسی داشته باشیم
        self.player = 1  # بازیکن "X" اول بازی را شروع می کند
        self.ai = -1  # بازیکن "O" که نرمالا کامپیوتر است
        self.moves = [i for i in range(SIZE ** 2)]

        # دکمه‌های بازی
        self.buttons = [[QPushButton(self) for _ in range(SIZE)] for _ in range(SIZE)]
        for i in range(SIZE):
            for j in range(SIZE):
                self.buttons[i][j].setFixedSize(80, 80)
                # self.buttons[i][j].clicked.connect(lambda _, i=i, j=j: self.mark(i, j))
                # self.buttons[i][j].setFont(self.font)
                self.buttons[i][j].setStyleSheet("QPushButton { font: bold 48px; }")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TicTacToe()
    ex.show()
    sys.exit(app.exec_())