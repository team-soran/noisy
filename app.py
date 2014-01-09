# -*- coding: utf-8 -*-
from sys import exit, argv

from PySide.QtGui import QApplication

from noisy.window import NoisyWindow

def main():
    app = QApplication(argv)
    win = NoisyWindow()
    exit(app.exec_())

if __name__ == '__main__':
    main()
