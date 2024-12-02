import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Membuat simbol-simbol yang diperlukan
x = sp.symbols('x')

# Mendefinisikan fungsi
f = (x**2 - 1) / (x )

# Menghitung limit ketika x mendekati 1
limit_x1 = sp.limit(f, x, 1)

# Membuat array x dan array y untuk plot
step = 0.01
x_values = np.arange(0, 2 + step, step)
y_values = [sp.limit(f, x, xi) for xi in x_values]

# Membuat plot
plt.plot(x_values, y_values, label=f'Limit as x -> 1: {limit_x1}', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
