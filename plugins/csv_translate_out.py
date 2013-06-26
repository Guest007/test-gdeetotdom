#! -*- coding: utf-8 -*-

"""Translated to english CSV export with header"""

# imports
import sys
import csv
import base


class csvTranslatedExport(base.baseplugin):
    """Write CSV with field translation"""

    def __init__(self):
        pass

    def run(self):
        return ("csv_translated", __doc__)

    def write(self, data_to_save, outfile="out1.csv"):
        """need iterable data. Outfile - optional"""

        with open(outfile, 'wb') as f:
            writer = csv.writer(f, delimiter=';')
            for n in data_to_save:
                writer.writerow(self.translate(n))


if __name__ == '__main__':
    a = csvTranslatedExport()
    b = ("комната", 15)
    print a.translate(b)
    # status = main("../test/1.csv")
    sys.exit()
