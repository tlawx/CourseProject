import csv
from os import stat
import pandas

class CSVParser:
    def __init__(self, filename):
        self.filename = filename

    @staticmethod
    def readfile_to_dict(filename):
        lines = []
        with open(filename, mode='r', encoding='utf-8-sig') as csv_file: # changed encoding from 'UTF8' to 'utf-8-sig'
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for l in csv_reader:
                lines.append(l)
        return lines


    @staticmethod
    def readfile_to_df(filename):
        df = pandas.read_csv(filename)
        return df

    @staticmethod
    def check_file_path():
        pass


    