# Import  Libraries
import numpy as np
import matplotlib.pyplot as plt

# Body

n = np.linspace(0, 4*np.pi, 100)
sin = np.sin(n)
plt.plot(n, sin)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Sin Wave")
plt.xlim([0, 4*np.pi])
plt.ylim(-1.5, 1.5)
plt.show()
