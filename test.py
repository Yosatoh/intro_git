import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print('program start') 

x = np.arange(-3, 3, 0.01)
y = np.sin(x)

plt.plot(x, y)
plt.grid()
plt.show()

