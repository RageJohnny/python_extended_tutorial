import numpy as np
import matplotlib.pyplot as plt

# Einführung in Numpy und Matplotlib
random_numbers = np.random.rand(100)
plt.hist(random_numbers)
plt.title('Histogramm von 100 Zufallszahlen')
plt.show()