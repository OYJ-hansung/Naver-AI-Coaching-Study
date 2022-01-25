import csv

file_path = "./data-01-test-score.csv"  # 파일 경로


class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        data = []  # 전체 담을 리스트
        with open(self.file_path, "r", encoding="cp949") as score_file:  # csv 파일을 score_file 객체에 저장
            csv_data = csv.reader(score_file)  # csv_data 읽기
            for row in csv_data:  # 읽어온 데이터를 한 줄씩 처리
                data.append(row)
        return data


read_csv = ReadCSV(file_path)
print(read_csv.read_file())
