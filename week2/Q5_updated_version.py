import os
import csv

class ReadCSV():
    '''
    class ReadCSV는 멤버 변수로 CSV파일경로: str, CSV파일정보: list[list[int]] 형태로 갖는다.
    올바른 파일경로를 받을 경우, CSV파일정보: list[list[int]] 형태로 저장
    존재하지 않은 파일경로를 받을 경우, CSV파일경로 = None, CSV파일정보 = None
    올바르지 않은 파일경로를 받을 경우, ValueError
    '''
    def __init__(self, file_path: str):
        """file_path를 .csv로 읽고, list[list[int]]로 저장

        Args:
            file_path (str): 파일경로
        """
        self.file_path = file_path
        self.lst = None
        if os.path.isfile(file_path):
            self.lst = self.read_file()

    def read_file(self):
        """self.file_path를 .csv로 읽는다.

        Returns:
           list[list[int]] : self.file_path의 정보
        """
        if not os.path.isfile(self.file_path):
            return None
        ret = []
        with open(self.file_path, 'r') as csv_file:
            csv_data = csv.reader(csv_file)
            for line in csv_data:
                ret.append(list(map(int, line)))
        return ret

    def merge_list(self):
        """self.lst의 평균값들의 오름차순
            self.lst는 변경하지 않는다.

        Returns:
           list[float] : self.lst의 평균값들의 오름차순
        """
        if not self.lst:
            return None
        ret = []
        for each_lst in self.lst:
            print(sum(each_lst) / len(each_lst))
            ret.append(sum(each_lst) / len(each_lst))
        return sorted(ret)


if __name__ == '__main__':
    invalid_path = "invalid_file"
    invalid_read = ReadCSV(invalid_path)
    print(invalid_read.read_file())
    print(invalid_read.merge_list())

    file_path = "data-01-test-score.csv"
    read_csv = ReadCSV(file_path)
    print(read_csv.read_file())
    read_csv.merge_list()