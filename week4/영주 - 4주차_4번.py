import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'r--', t, t**2, 'gs', t, t**3, 'b^')

# T 데이터로 다음과 같은 3가지 plot을 그린다.
# t, t, 'r--' >> f(t) = t (red dash)
# t, t**2, 'gs' >>  f(t) = t^2 (blue square)
# t, t**3, 'b^' >>  f(t) = t^3 (green triangle)

plt.show()