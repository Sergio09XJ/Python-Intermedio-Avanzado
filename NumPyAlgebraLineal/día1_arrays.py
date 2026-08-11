
import numpy as np 
array_1 = np.array([1,2,3,4,5,6,7,8,9,10])

#Su shape es de 10, porque tiene 10 columnas
print(f"\nArreglo 1 es: \n {array_1} | shape: {array_1.shape} \n | ndim: {array_1.ndim} | size: {array_1.size} | dtype: {array_1.dtype}")

matriz_3x3 = np.array([[1,2,3], [4,5,6], [7,8,9]])
#Su shape es de 3,3 | 3 Filas y 3 Columnas 
print(f"\nMatriz 3 x 3: \n {matriz_3x3} \n  | shape: {matriz_3x3.shape} | ndim: {matriz_3x3.ndim} | size: {matriz_3x3.size} | dtype: {matriz_3x3.dtype}")

matrix_4x4 = np.zeros((4,4))
#Su shape es de 4,4 | 4 Filas y 4 Columnas
print(f"\nMatriz 4x4 de ceros: \n {matrix_4x4} \n | shape: {matrix_4x4.shape} | ndim: {matrix_4x4.ndim} | size: {matrix_4x4.size} | dtype: {matrix_4x4.dtype}")

matrix_2x5 = np.ones((2,5))
#Su shape es de 2,5 | 2 Filas y 5 Columnas
print(f"\nMatriz 2x5 de unos: \n {matrix_2x5} \n | shape: {matrix_2x5.shape} | ndim: {matrix_2x5.ndim} | size: {matrix_2x5.size} | dtype: {matrix_2x5.dtype}")

space_array_20 = np.linspace(0,1,20)
#Su shape es de 20 | 20 Columnas
print(f"\nArray de 0 a 1 con 20 números: \n {space_array_20} \n | shape: {space_array_20.shape} | ndim: {space_array_20.ndim} | size: {space_array_20.size} | dtype: {space_array_20.dtype}")

matriz_3x3x3 = np.zeros((3,3,3))
print(f"\nMatriz de 3 dimensiones \n {matriz_3x3x3} \n | shape: {matriz_3x3x3.shape} | ndim: {matriz_3x3x3.ndim} | size: {matriz_3x3x3.size} | dtype: {matriz_3x3x3.dtype}")