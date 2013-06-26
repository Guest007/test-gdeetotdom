#!/bin/bash

# testing all 4 variant
python convert.py --source_path="test/1.csv" --plugin=csv_simple
python convert.py --source_path="test/1.csv" --plugin=csv_translated
python convert.py --source_path="test/1.csv" --plugin=xml_simple
python convert.py --source_path="test/1.csv" --plugin=xml_complex

# show usage
python convert.py




