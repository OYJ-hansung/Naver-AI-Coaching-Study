"""
np.random.random() 은 0부터 1까지의 난수를 배열로 저장시키는 함수 
dot은 arr1과 arr2의 행렬곱 즉, 행렬 내적 연산을 의미
"""
import numpy as np
arr1 = np.random.random((5,3))
arr2 = np.random.random((3,2))
dot = arr1@arr2
print(dot,dot.shape)