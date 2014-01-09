# -*- coding: utf-8 -*-
from PySide.QtGui import QTableWidget, QTableWidgetItem, QWidget
from PySide.QtCore import Qt

class MainWidget(QWidget):

    def __init__(self, window=None):
        super(MainWidget, self).__init__(window)
        self.setGeometry(0, 20, 500, 500)
        self.show()


class MusicTableWidget(QTableWidget):

    def __init__(self, w=None):
        super(MusicTableWidget, self).__init__(w)
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels([u'가수', u'제목', u'앨범'])

    def append(self, l):
        r = self.rowCount()
        self.insertRow(r)
        for i, x in enumerate(l):
            item = QTableWidgetItem("%s" % x)
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            self.setItem(r, i, item)
