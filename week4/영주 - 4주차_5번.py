import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c'] #그래프 이름 리스트입니다. 
values = [1, 10, 100] #그래프읟 데이터값에 해당하는 리스트입니다.

plt.figure(figsize=(9, 3))

plt.subplot(131) # plot을 1행 3열 모양으로 나눈후, 첫번째 칸에 해당하는 subplot을 지정합니다.
plt.bar(names, values) # bar plot입니다.
plt.subplot(132) # 두번째 칸에 해당하는 subplot을 지정합니다.
plt.scatter(names, values) # scatter plot입니다.
plt.subplot(133) # 세번째 칸에 해당하는 subplot을 지정합니다.
plt.plot(names, values) # plt.plot의 default인 line plot입니다.

plt.suptitle('Categorical Plotting') # plot의 제목입니다.
plt.show()# plot을 출력합니다.