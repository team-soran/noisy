# -*- coding: utf-8 -*-
from sys import exit, argv
from os import walk
from json import dumps

from PySide.QtGui import QApplication, QMainWindow, QFileDialog, QAction, QIcon

class ImportDirAction(QAction):

    def __init__(self, w):
        super(ImportDirAction, self).__init__(
            QIcon('exit.png'), u'&음악 폴더 지정', w)
        self.files = []
        self.setShortcut('Ctrl+O')
        self.dialog = QFileDialog(w)
        self.dialog.setFileMode(QFileDialog.Directory)
        self.dialog.setOption(QFileDialog.ShowDirsOnly)
        self.triggered.connect(self.choose_dir)

    def choose_dir(self):
        if self.dialog.exec_():
            self.dirs = self.dialog.selectedFiles()
            self.import_mp3()

    def import_mp3(self):
        for path in self.dirs:
            for root, dirs, files in walk(path):
                for f in files:
                    if 'mp3' in f:
                        self.files.append('%s\\%s' % (root, f))
        with open('./dirs.json', 'w') as f:
            f.write(dumps(self.dirs))


class NoisyWindow(QMainWindow):

    def __init__(self):
        super(NoisyWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 250, 150)
        import_dir = ImportDirAction(self)
        menu = self.menuBar()
        self.menu_f = menu.addMenu(u'&파일')
        self.setWindowTitle('window')
        self.show()

    @property
    def menu_file(self):
        return self.menu_f

    @menu_file.setter
    def menu_file(self, v):
        self.menu_f.addAction(v)


def addMenus(win):
    win.menu_file = ImportDirAction(win)


def main():
    app = QApplication(argv)
    win = NoisyWindow()
    addMenus(win)
    exit(app.exec_())

if __name__ == '__main__':
    main()
