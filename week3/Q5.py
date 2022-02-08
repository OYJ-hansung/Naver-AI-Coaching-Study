import numpy as np

xy = np.array([[1., 2., 3., 4., 5., 6.], [10., 20., 30., 40., 50., 60.]])

# 각 변수에 x축과 y축의 주소를 저장한다.
x_train = xy[0]
y_train = xy[1]

beta_gd = np.random.rand(1)	# 임시 기울기
bias = np.random.rand(1)	# 임시 절편

learning_rate = 0.01		# 학습률

for i in range(1000):
	pred = beta_gd * x_train + bias 						# 예측값 wx+b
	error = sum(np.square(pred - y_train)) / len(y_train)	# MSE mean

	gd_w = sum(np.multiply(pred - y_train, 2 * x_train)) / len(y_train)	# MSE 미분값
	gd_b = sum(np.multiply(pred - y_train, 2)) / len(y_train)			# MSE 미분값
	
	beta_gd -= learning_rate * gd_w	# 기울기 조정
	bias -= learning_rate * gd_b	# 절편 조정
	
	if i % 100 == 0: # 100번마다 출력
		print(f'Epoch ({i:10d}/1000) cost: {error:10f}, w: {beta_gd.item(0):10f}\
			,b: {bias.item(0):10f}')