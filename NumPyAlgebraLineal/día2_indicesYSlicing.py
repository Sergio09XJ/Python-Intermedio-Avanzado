import numpy as np

matriz = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

print(f"\nEl número 7: {matriz[1,2]}") #Num 7 
print(f" La tercera Fila: \n {matriz[2]}") #Tercera Fila
print(f" La segunda Columna: \n {matriz[:, 1:2]}") #Segunda Columna
print(f"Las dos primeras Filas: \n  {matriz[0:2, :]}") #Dos primeras filas
print(f"Las dos ultimas Columnas: \n {matriz[:, 2:]}") #Las dos ultimsas columnas
print(f"La submatriz [[6,7],[10,11]]: \n {matriz[1:3,1:3]}")#La submatriz [[6,7],[10,11]]
print(f"Valores pares de la matriz: \n {matriz[matriz% 2 == 0]}")#Valores pares de matriz

matriz[1:3, 1:3] = 0 #Modificamos la matriz
print(f"Matriz modificada = \n{matriz}")