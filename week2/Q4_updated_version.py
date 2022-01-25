import csv
from pprint import pprint

class ReadCSV():

    def __init__(self, file_path :str):
        self.file_path = file_path
        self.lst = self.read_file()
        
    def read_file(self):
        data_set = []
        with open(self.file_path, "r", encoding="cp949") as p_file:
            csv_data = csv.reader(p_file)
            for row in csv_data:
                data_set.append(list(map(int, row)))                           
        return data_set
        
    def merge_list(self):
        data_set = []       
        for row in self.lst:
            data_set.append(sum(row))
                               
        return data_set

filepath = "./data-01-test-score.csv"
read_csv = ReadCSV(filepath)
pprint(read_csv.read_file())
print(read_csv.merge_list())
