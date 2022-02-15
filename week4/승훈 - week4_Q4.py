import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

#x,y,색상 값을넣어 plot그래프를 생성한다.
plt.plot(t, t, 'r--', t, t**2, 'gs', t, t**3, 'b^')
#생성된 그래프를 flush한다.
plt.show()