import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]
#최초 장의 크기 가로 9 세로 3으로 설정
plt.figure(figsize=(9, 3))

# subplot : 한 화면에 여러 그래프 나눠서 그림
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.show()