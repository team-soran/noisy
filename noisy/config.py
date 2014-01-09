# -*- coding: utf-8 -*-
from os import walk
from os.path import exists
from json import dumps, loads

__all__ = 'NoisyConfig',


class NoisyConfig(object):
    _dir_loc = './dir.json'

    def __init__(self):
        self._dir = self.dir_from_file()
        self._mp3 = []

    def dir_from_file(self):
        r = []
        if exists(self._dir_loc):
            with open(self._dir_loc, 'r') as f:
                r = loads(f.read())
        return r

    def mp3_from_dir(self):
        r = []
        for path in self.dir:
            for root, dirs, files in walk(unicode(path)):
                for f in files:
                    if f.endswith('mp3'):
                        r.append(u'%s\\%s' % (root, f))
        return r

    @property
    def dir(self):
        return self._dir

    @dir.setter
    def dir(self, o):
        if not isinstance(o, basestring):
            raise Exception(
                'directory must be `string` not %s.' % type(o))
        self._dir.append(o)
        self._dir = list(set(self._dir))
        with open(self._dir_loc, 'w') as f:
            f.write(dumps(self._dir).encode('utf-8'))

    @property
    def mp3(self):
        if not self._mp3:
            self._mp3 = self.mp3_from_dir()
        return self._mp3
