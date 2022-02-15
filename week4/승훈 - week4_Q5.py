import matplotlib.pyplot as plt

names = ['group_a', "group_b", 'group_c']
values = [1, 10, 100]

#figure은 그래프를 그리는 탬플릿,배경 같은것, 크기 조절을figsize로 가능
plt.figure(figsize=(9,3))

#subplot는 여러개의 그래프를 하나의 그림에 나타내도록 하는 함수
#subplot(row, column, index)
plt.subplot(1,3,1)
plt.bar(names, values)
plt.subplot(1,3,2)
plt.scatter(names, values)
plt.subplot(1,3,3)
plt.plot(names,values)
plt.suptitle('Categorical Plotting')
plt.show()