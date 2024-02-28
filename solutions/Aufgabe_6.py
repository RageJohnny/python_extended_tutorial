import numpy as np
import matplotlib.pyplot as plt

# Generiere einen optisch beeindruckenden Output
x = np.linspace(0, 10, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label='Sinus')
plt.plot(x, y_cos, label='Kosinus', linestyle='--')
plt.xlabel('X Achse')
plt.ylabel('Y Achse')
plt.title('Sinus und Kosinus Kurven')
plt.legend()
plt.show()