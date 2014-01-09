# -*- coding: utf-8 -*-
from PySide.QtGui import QMainWindow, QVBoxLayout, QPushButton

from .menu import ImportDirAction
from .widget import MusicTableWidget, MainWidget

__all__ = 'NoisyWindow',

class NoisyWindow(QMainWindow):

    def __init__(self):
        super(NoisyWindow, self).__init__()
        self.init_ui()
        self.init_menu()

    def init_ui(self):
        self.setGeometry(20, 20, 500, 800)
        self.menu = self.menuBar()
        wid = MainWidget(self)
        layout = QVBoxLayout()
        play_button =  QPushButton("Play")
        self.table = MusicTableWidget()
        layout.addWidget(play_button)
        layout.addWidget(self.table)
        wid.setLayout(layout)
        self.setWindowTitle(u'Noisy - 소란스러운 음악 플레이어')
        self.show()

    def init_menu(self):
        self.menu_file = self.menu.addMenu(u'&파일')
        self.menu_file.addAction(ImportDirAction(self))
