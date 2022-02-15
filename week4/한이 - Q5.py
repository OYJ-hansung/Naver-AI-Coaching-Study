import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

# subplot : 여러 개의 그래프를 하나의 그림에 나타내게 함
plt.subplot(1, 3, 1)
plt.bar(names, values)
plt.subplot(1, 3, 2)
plt.scatter(names, values)
plt.subplot(1, 3, 3)
plt.plot(names, values)
plt.show()
