# define the function
import math
import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return np.exp(x)

x = np.linspace(-5,5,100)
y = f(x)
print(x)
print(y)
plt.plot(x,y)
plt.show()

