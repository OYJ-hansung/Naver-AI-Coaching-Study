import pandas as pd
idx = ["HDD", "SSD", "USB", "CLOUD"]
data = [19, 11, 5, 97]

#series : 어떤 데이터 타입이든 보유할 수 있는 레이블링된 1차원 배열
series = pd.Series(data=data, index=idx)

# 10이상 20 이하 가지는 데이터
series = series[series >= 10][series <= 20]

print(series)