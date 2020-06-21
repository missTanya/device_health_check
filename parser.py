# /usr/bin/python

#parser_csv-to-dict.py

import csv
import pprint

def csv_in_parser(file):
    """This accepts passed file in csv format
    """
    print('PARSER saying hello...')
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for line in csv_reader:
            print(line)
            k = line[0]
            v = line[1]
            dict_temp = { line[0]:line[1] for line in csv_reader }
        return dict_temp
