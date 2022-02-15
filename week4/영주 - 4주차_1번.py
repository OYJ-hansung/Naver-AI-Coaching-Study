import pandas as pd

idx = ["HDD", "SSD", "USB", "CLOUD"]
data = [19, 11, 5, 97]

series = pd.Series(data, index=idx)# 판다스의 시리즈는 인덱스가 자동으로 따라붙게 되는데, 이때 인덱스 리스트를 지정해줍니다.
print(series)

series = series[series>=10][series <=20]# 시리즈에서 주어진 조건에 만족하는 값을 추출합니다.
print(series)
