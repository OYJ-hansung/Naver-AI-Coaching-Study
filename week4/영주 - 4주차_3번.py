import pandas as pd

idx = ["Sue", "Ryan", "Jay", "Jane", "Anna"]
col = ["round_1", "round_2", "round_3", "round_4", "round_5"]
data = [[55, 65, 60, 66, 57],
        [64, 77, 71, 79, 67],
        [88, 81, 79, 89, 77],
        [45, 35, 30, 46, 47],
        [91, 96, 90, 97, 99]]
print()
df = pd.DataFrame(data, index=idx, columns=col) # 인덱스와 열에 해당하는 리스트를 지정해주고 데이터를 포함한 새로운 데이터프레임을 생성합니다.
col_round_6 = pd.Series([11, 15, 13, 17, 19], index=idx) # 새로운 열 round_6를 Series함수를 이용해 생성합니다.
print(df)
print()
df["round_6"] = col_round_6 # 데이터프레임이 round_6열을 추가합니다.
print(df)
print()
print(df.describe().loc[["mean", "max", "min"]]) # 각 열의 mean, max, min을 출려합니다.
