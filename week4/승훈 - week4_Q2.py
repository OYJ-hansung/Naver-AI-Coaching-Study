import pandas as pd

df1 = pd.DataFrame([\
                    ["cherry","Fruit",100],\
                    ["mango","Fruit",110],\
                    ["potato","Vegetable",60],\
                    ["onion","Vegetable",80]],\
                    columns=["Name","Type","Price"])

df2 = pd.DataFrame([\
                    ["pepper","Vegetable", 50],\
                    ["carrot","Vegetable", 70],\
                    ["banana", "Fruit", 90],\
                    ["kiwi","Fruit",120]],\
                    columns=["Name","Type","Price"])

# df1, df2를 colums를 이용해 결합
# axis값을 주면 index에 맞춰 옆으로 데이터를 배열할수있다.
df3 = pd.concat([df1,df2], axis=1)
print(df3)

df3 = pd.concat([df1,df2])
print(df3)
#Type Fruit에 따라 정렬
df_fruit = df3.loc[df3["Type"] == "Fruit"]
#print(df_fruit)
#가격순으로 정리 가격을 기준으로 ascending=false일 경우 내림차순
df_fruit = df_fruit.sort_values(by="Price", ascending=False)
print(df_fruit)

df_veg = df3.loc[df3["Type"] == "Vegetable"]
df_veg = df_fruit.sort_values(by="Price", ascending=False)
print(df_veg)

# Fruits와 Vegetable 상위 2개의 가격의 합을 출력
print("Sum of Top 2 Fruit Price :", sum(df_fruit[:2]["Price"]))
print("Sum of Top 2 Vegetable Price :", sum(df_veg[:2]["Price"]))