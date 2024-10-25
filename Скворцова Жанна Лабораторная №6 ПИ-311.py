from statistics import LinearRegression
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import sklearn.linear_model as lr
import numpy as np
import math
fahrenheit =[[-88.6], [-29.2], [32.0], [93.2], [129.2], [152.6], [212.0]]
kelvin = [[206.15], [213.15], [273.15], [307.15], [327.15], [340.15], [373.15]]
plt.figure(figsize=(15,8), dpi = 50)
plt.scatter(fahrenheit, kelvin, label = 'Входные значения', color = 'green', marker = '$f$');
plt.xlabel('fahrenheit')
plt.ylabel('kelvin')
plt.legend()
plt.grid(True)

for f, k in zip(fahrenheit, kelvin):
    print(f'фаренгейт {f} = {k} кельвин')

lr = LinearRegression()
lr.fit(fahrenheit, kelvin)
lr.predict([[256], [123]])
lr.coef_
lr.intercept_
fahrenheit_test = [[-100], [100], [-200], [-273], [10], [70], [87]]
kelvin_test = lr.predict(fahrenheit_test)
kelvin_test
for f,k in zip(fahrenheit_test, kelvin_test):
    print(f'фаренгейт {f} = {k} кельвин')
x_range = np.arange(-94, 248)
y_range = (x_range+459.67) * 5 / 9
plt.figure(figsize=(15,8), dpi= 280)
plt.plot(x_range, y_range, label = 'Уравнение', linewidth = '1')
plt.scatter(fahrenheit, kelvin, label = 'Входные данные', color = 'green')
plt.scatter(fahrenheit_test, kelvin_test, label = 'Предсказанное значение', color = 'blue')
plt.xlabel('Фаренгейт')
plt.ylabel('Кельвин')
plt.legend()
plt.grid(True)
plt.show()
print('Число Эйлера:', math.e)
print('Число пи:', math.pi)
print(math.nan)
print("Факториал 17:", math.factorial(17))
print('Наибольший делитель 128 и 17:', math.gcd(128, 17))