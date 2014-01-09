# -*- coding: utf-8 -*-
from PySide.QtGui import QFileDialog, QAction, QIcon

from .config import NoisyConfig

__all__ = 'ImportDirAction',

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
            config = NoisyConfig()
            for dir in self.dialog.selectedFiles():
                config.dir = dir
