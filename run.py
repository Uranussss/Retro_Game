# coding=utf-8

import sys
import random
import argparse
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from main import Tetris


parser = argparse.ArgumentParser()
parser.add_argument('--value_of_speed', default='300')


class UI(QMainWindow):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed

        self.initUI()  # edit the UI, using this function named initUI

    def initUI(self):
        # set the typeface
        QToolTip.setFont(QFont('SansSerif', 10))

        # tip for blank area
        self.setToolTip('This is a Tetris game')

        # play
        self.start = QPushButton('start', self)
        self.start.setToolTip('start the tetris game!')
        self.start.setGeometry(140, 150, 300, 20)

        # for child windows of start
        layout = QVBoxLayout()
        layout.addWidget(self.start)
        self.setLayout(layout)

        # set window size
        self.resize(600, 440)
        self.setWindowTitle('Teteris')
        # set the icon of this window, using the picture named tetris.jpg in this project.
        self.setWindowIcon(QIcon('tetris.jpg'))
        self.center()

        # show this window automatically
        self.show()

    # rewrite this function: have a new window to confirm whether people want to exit this game
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # center the window
    def center(self):

        # catch the window
        qr = self.frameGeometry()
        # get the center point
        cp = QDesktopWidget().availableGeometry().center()
        # print
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    from AI_agent import TETRIS_AI
    args = parser.parse_args()
    # show windows, and create a correlation between these windows
    print("would you like to play this Tetris game? Type '1' or '0' please.")
    choice = input()
    if choice == '1':
        print("would you like to watch AI playing? Type '1' or '0' please.")
        watch = input()
        if watch == '1':
            ai = TETRIS_AI
            speed = 20
        else:
            ai = None
            speed = int(args.value_of_speed)
        app = QApplication(sys.argv)
        new = Tetris(speed, ai)
        ex = UI(speed)
        ex.start.clicked.connect(new.show)
        sys.exit(app.exec_())
    else:
        print("goodbye!")
