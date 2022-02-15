import pandas as pd

idx = ["HDD", "SSD","USB","CLOUD"]
data = [19,11,5,97]

#data,index를 지정해서 series생성
series = pd.Series(data, index=idx)
#print(series)
#data중에 10보다크거나 같고, 20보다 같거나 작은 값만 저장
series = series[series >=10][series <=20]

print(series)