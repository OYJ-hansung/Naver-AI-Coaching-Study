import numpy as np
import matplotlib.pyplot as plt
# 0.2 간격으로 생성
t = np.arange(0., 5., 0.2)

#빨간 대쉬. 녹색 사각형 , 파란 삼각형
plt.plot(t, t, 'r--',t , t**2, 'gs',t,t**3,'b^')
plt.show()