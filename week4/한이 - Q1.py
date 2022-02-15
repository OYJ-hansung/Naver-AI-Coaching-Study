import pandas as pd

idx = ["HDD", "SSD", "USB", "CLOUD"]
data = [19, 11, 5, 97]

# Series로 구현
series = pd.Series(data=data, index=idx)

# 10이상 20이하
series = series[series >= 10][series <= 20]

print(series)
