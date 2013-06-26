#! -*- coding: utf-8 -*-

"""Simple XML output"""

# imports
import sys
import xml.etree.ElementTree as ET
import base


class xmlSimpleExport(base.baseplugin):
    """Write simple XML with field translation"""

    def __init__(self):
        pass

    def run(self):
        return ("xml_simple", __doc__)

    def write(self, data_to_save, outfile="out.xml"):
        """need iterable data. Outfile - optional"""
        root = ET.Element('root')

        # get first line (header) and translate
        header = self.translate(data_to_save.next())

        for elem in data_to_save:
            # get each line and translate
            attr = self.translate(elem)
            ad = ET.SubElement(root, 'ad',
                            attrib={header[0]: attr[0], header[1]: attr[1]})
        tree = ET.ElementTree(root)
        tree.write(outfile)


# def main(pathandfile):
#     """This function just for test"""
#     getfile = csv_open(pathandfile)
#     for row in getfile:
#         print ' '.join(row)
#     return 0

if __name__ == '__main__':
    # status = main("../test/1.csv")
    sys.exit()
