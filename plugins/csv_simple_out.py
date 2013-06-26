#! -*- coding: utf-8 -*-

"""Simple CSV export - without header"""

# imports
import sys
import csv
import base


class csvSimpleExport(base.baseplugin):
    """Simple CSV write - without header"""

    def __init__(self):
        pass

    def run(self):
        return ("csv_simple", __doc__)

    def write(self, data_to_save, outfile="out.csv"):
        """need iterable data. Outfile - optional"""
        with open(outfile, 'wb') as f:
            writer = csv.writer(f, delimiter=';')
            i = 0
            # Header will be skipped
            for n in data_to_save:
                if i > 0:
                    writer.writerow(n[::-1])
                i += 1


# def main(pathandfile):
#     """This function is just for test"""
#     c = csvSimpleExport()
#     c.csv_write(pathandfile, data_save)
#     return 0


if __name__ == '__main__':
    # status = main("../test/2.csv")
    sys.exit()
