import csv
from pprint import pprint
data_set = []


def read_file(file_path):
    rownum = 0
    with open(file_path, "r", encoding="cp949") as p_file:
        csv_data = csv.reader(p_file)
        for row in csv_data:
            data_set.append(row)
            rownum += 1
    return data_set

file_path = "./data-01-test-score.csv"

read_csv = read_file(file_path)

pprint(read_csv)
