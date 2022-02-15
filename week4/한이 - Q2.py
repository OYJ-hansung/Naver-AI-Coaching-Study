import pandas as pd

df1 = pd.DataFrame([["cherry", "Fruit", 100],
                    ["mango", "Fruit", 110],
                    ["potato", "Vegetable", 60],
                    ["onion", "Vegetable", 80]],
                   columns=["Name", "Type", "Price"])

df2 = pd.DataFrame([["pepper", "Vegetable", 50],
                   ["carrot", "Vegetable", 70],
                   ["banana", "Fruit", 90],
                   ["kiwi", "Fruit", 120]],
                   columns=["Name", "Type", "Price"])

df3 = pd.concat([df1, df2])

# loc는 index 이름
df_fruit = df3.loc[df3["Type"] == "Fruit"]
df_fruit = df_fruit.sort_values(by="Price", ascending=False)
#print(df_fruit)

df_veg = df3.loc[df3["Type"] == "Vegetable"]
df_veg = df_veg.sort_values(by="Price", ascending=False)
#print(df_veg)

print("Sum of Top 2 Fruit Price :", sum(df_fruit[:2]["Price"]))
print("Sum of Top 2 Vegetable Price :", sum(df_veg[:2]["Price"]))