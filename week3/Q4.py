import numpy as np

xy = np.array([[1., 2., 3., 4., 5., 6.], [10., 20., 30., 40., 50., 60.]])

x_train = xy[0]
y_train = xy[1]

beta_gd = np.random.rand(1)
bias = np.random.rand(1)

print(beta_gd, bias)

'''
np.random.randn
: 각 구간의 샘플수(난수의 개수)가 정규분포를 따르도록 생성
np.random.rand
: 각 구간의 샘플 수(난수의 개수)가 거의 동일하도록 생성
'''


