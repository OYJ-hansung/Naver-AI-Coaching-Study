from turtle import color
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0., 5., 0.2)

plt.plot(t, t, color="r", linestyle="--")
plt.plot(t, t**2, 'gs')
plt.plot(t, t**3, 'b^')
plt.show()
