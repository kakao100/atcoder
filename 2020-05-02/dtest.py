import matplotlib.pyplot as plt
import numpy as np
a = 5
b = 7
width = 1000
x = np.arange(1,10000,1)
y = np.ceil((a * x) // b)  - a * np.ceil(x // b)

plt.plot(x,y)
plt.show()
