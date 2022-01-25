import csv
from pprint import pprint

class ReadCSV():

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        rownum = 0
        data_set = []
        
        with open(self.file_path, "r", encoding="cp949") as p_file:
            csv_data = csv.reader( p_file ,delimiter=',', quoting=csv.QUOTE_ALL )
            for row in csv_data:
                Ltoi=[]
                for change in row:
                    Ltoi.append(int(change))
                data_set.append(Ltoi)
                rownum += 1
        return data_set
        
    def merge_list(self):
        rownum = 0
        data_set = []       
        with open(self.file_path, "r", encoding="cp949") as p_file:
            csv_data = csv.reader( p_file ,delimiter=',', quoting=csv.QUOTE_ALL )
            for row in csv_data:
                Ltoi=[]
                for change in row:
                    Ltoi.append(int(change))
                data_set.append(sum(Ltoi))
                rownum += 1
        return data_set

filepath = "./data-01-test-score.csv"
read_csv = ReadCSV(filepath)
pprint(read_csv.read_file())
print(read_csv.merge_list())
