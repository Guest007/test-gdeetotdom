#! -*- coding: utf-8 -*-

"""Complex XML output"""

# imports
import sys
import xml.etree.ElementTree as ET
import base


class xmlComplexExport(base.baseplugin):
    """Write more complex XML"""

    def __init__(self):
        pass

    def run(self):
        return ("xml_complex", __doc__)

    def write(self, data_to_save, outfile="out1.xml"):
        """need iterable data. Outfile - optional"""
        root = ET.Element('root')

        # get first line (header) and translate
        header = self.translate(data_to_save.next())

        for elem in data_to_save:
            ad = ET.SubElement(root, 'ad')
            tr = ET.SubElement(ad, header[0])
            tr.text = elem[0].decode("utf-8")
            fs = ET.SubElement(ad, header[1])
            fs.text = elem[1].decode("utf-8")

        tree = ET.ElementTree(root)
        tree.write(outfile, encoding="utf-8")


# def main(pathandfile):
#     """This function just for test"""
#     getfile = csv_open(pathandfile)
#     for row in getfile:
#         print ' '.join(row)
#     return 0

if __name__ == '__main__':
    # status = main("../test/1.csv")

    sys.exit()
