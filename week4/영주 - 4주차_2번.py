import pandas as pd

df1 = pd.DataFrame([
                    ["cherry", "Fruit", 100],
                    ["mango", "Fruit", 110],
                    ["poatato", "Vegetable", 60],
                    ["onion", "Vegetable", 80]],
                    columns=["Name", "Type","Price"]) 
    
df2 = pd.DataFrame([
                    ["pepper", "Vegetable", 50],
                    ["carrot", "Vegetable", 70],
                    ["banana", "Fruit", 90],
                    ["kiwi", "Fruit", 120]],
                    columns=["Name", "Type","Price"]) 

df3 = pd.concat([df1, df2], axis=0) # 두개의 데이터프레임을 axis 0 방향으로 결합한 새로운 데이터프레임 생성
print()
print(df3)

df_fruit = df3.loc[df3["Type"] == "Fruit"] # 새로운 데이터프레임으로부터 Type이 과일이 데이터만 가져온 과일 데이터프레임 생성
df_fruit = df_fruit.sort_values(by="Price", ascending=False) # 내림차순 정렬
print()
print(df_fruit)

df_veg = df3.loc[df3["Type"] == "Vegetable"] # 새로운 데이터프레임으로부터 Type이 야채이 데이터만 가져오기 야채 데이터프레임 생성
df_veg = df_veg.sort_values(by="Price", ascending=False) # 내림차순 정렬
print()
print(df_veg)

print()
print("Sum of Top 2 Fruit Price : ", sum(df_fruit[:2]["Price"])) # 과일 데이터 프레임으로부터 가장 비싼(0, 1번 인덱스) 두개의 데이터 추출 및 합산
print("Sum of Top 2 Vegetable Price : ", sum(df_veg[:2]["Price"])) # 야체 데이터 프레임으로부터 가장 비싼(0, 1번 인덱스) 두개의 데이터 추출 및 합산
