#! -*- coding: utf-8 -*-

"""Import routines"""

# imports
import sys
import csv
import base


class cvsImport(base.baseplugin):
    def __init__(self):
        pass

    def run(self):
        pass

    def read(self, incfile):
        """Open file and yielding row"""
        with open(incfile, 'rb') as f:
            reader = csv.reader(f, delimiter=';')
            try:
                for row in reader:
                    yield row
            except csv.Error as e:
                sys.exit('file %s, line %d: %s' % (incfile, reader.line_num, e))


def main(pathandfile):
    """This function just for test"""
    csv_open = cvsImport()
    getfile = csv_open.read(pathandfile)
    for row in getfile:
        print ' '.join(row)
    return 0


if __name__ == '__main__':
    status = main("../test/1.csv")
    sys.exit()
