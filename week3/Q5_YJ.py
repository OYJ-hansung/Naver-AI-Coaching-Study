from re import X
import numpy as np

xy = np.array([[1, 2, 3, 4, 5, 6], [3, 6, 9, 12, 15, 18]], float)

x_train = xy[0]
y_train = xy[1]

beta_gd = np.random.rand(1)
bias = np.random.rand(1)

learning_rate = 0.01

for t in range(1000):
    error =  bias - X @ beta_gd
    grad = - np.transpose(X) @ error
    beta_gd = beta_gd - learning_rate * grad
    if i%100 == 0:
		print(f'Epoch ({i:10d}/1000) cost: {error:10f}, w: {beta_gd.item(0):10f}\,b: {bias.item(0):10f}')