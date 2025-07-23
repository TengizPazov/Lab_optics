import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
m1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
m2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

black = np.array([1.885, 2.5, 2.195, 2.31, 2.49, 2.67, 2.86, 3.10, 3.375, 3.74, 4.28, 5.01, 5.49, 5.83, 6.11, 6.39, 6.53, 6.71, 6.88, 7.03, 7.25, 7.32]) * 9.8
white = np.array([1.64, 1.775, 1.91, 2.09, 2.19, 2.37, 2.54, 2.74, 3.00, 3.22, 3.51, 4.10, 5.16, 5.69, 6.01, 6.19, 6.42, 6.61, 6.78, 6.99, 7.10, 7.23, 7.37, 7.495]) * 9.8

r_m_black = np.zeros(11)
r_m_white = np.zeros(12)

for i in range(11):
    r_m_black[i] = (black[21 - i] - black[i]) / 2

for i in range(12):
    r_m_white[i] = (white[23 - i] - white[i]) / 2

r_m_black = np.flip(r_m_black) # Убираем переворот
r_m_white = np.flip(r_m_white) # Убираем переворот
yerr = 0.2 * 9.8

print(r_m_black)

coefficients_black = np.polyfit(m1, r_m_black, 1)
polynomial_black = np.poly1d(coefficients_black)
coefficients_white = np.polyfit(m2, r_m_white, 1)
polynomial_white = np.poly1d(coefficients_white)

plt.figure(figsize=(12, 8))

# График для r_m_black с крестами погрешностей
plt.errorbar(m1, r_m_black, yerr=yerr, fmt='o', label='Данные Black')
plt.plot(m1, polynomial_black(m1), color='red', label=f'Аппроксимация Black: y = {coefficients_black[0]:.2f}x + {coefficients_black[1]:.2f}')

# График для r_m_white с крестами погрешностей
plt.errorbar(m2, r_m_white, yerr=yerr, fmt='x', label='Данные White')
plt.plot(m2, polynomial_white(m2), color='blue', label=f'Аппроксимация White: y = {coefficients_white[0]:.2f}x + {coefficients_white[1]:.2f}')

plt.xlabel('m, порядок', fontsize=12)
plt.ylabel('$r_{m}$', fontsize=12)
plt.title('Зависимость $r_{m}$ от m для Black и White', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True)
plt.show()