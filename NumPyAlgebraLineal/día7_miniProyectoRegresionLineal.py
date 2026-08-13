import numpy as np
import matplotlib.pyplot as plt
import random 

#Paso 1 creamos valores de x 
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

print(f"Valores de x:\n {x}")

#Paso 2 Generamos y con y = mx +b + ruido donde m = 3 y b = 5

ruido = np.random.normal(0, 5, size=x.shape)


y = (x * 3) + 5 + ruido

print(f"Valores de y: \n {y}")

#Paso 3 Construimos la Matriz X 


auxX =np.array([x, np.ones(20)])
X = auxX.T #Esto permite multiplicar X con la matriz [m,b] donde se multiplica cada la primera columna con m y la segunda b con 1 y se suman
           #Dando como resultado y = xm + 1(b) = b -> y = xm + b

print(f"Imprimimos la matriz X: \n {X}")

#Paso 4 encontrar Theta = [m,b] | Estos números nos permiten hacer la predicción 
#Para encontrar Theta usamos la formula ((X^T*X)^-1)X^T*y

theta = np.linalg.inv(X.T @ X) @ X.T @ y

print(f"Imprimimos theta: \n {theta}")

#Paso 5 y 6 Obtenemos el valor predicho = Estimación que hace el modelo  y comparamos con los valores reales.

y_predicha = np.matmul(X, theta)

print(f"\n Vemos y_predicha: \n{y_predicha}")
print(f"\n Vemos los valores reales y: \n{y}")

#Paso 7 Obtenemos MSE Función de Costo, nos permite ver que tan grande fue el margen de error de la predicción 

mse = np.mean((y - y_predicha)  ** 2)

print(f"\nLa tasa de error fue de: \n {mse}")

#Paso 8 Dibujamos la Gráfica: 

plt.scatter(x, y, color='blue', label = 'Datos Reales(y)')
plt.plot(x, y_predicha, color= 'red', linestyle='--', label='Predicción (y_hat)')

plt.title("Valores Reales(y) vs Predicción(y_predicha)")
plt.xlabel("Entrada (x)")
plt.ylabel("Salida (y)")
plt.legend()
plt.grid(True)

plt.show()
