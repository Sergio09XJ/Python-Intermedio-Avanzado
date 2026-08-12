import numpy as np 

A = np.arange(1,10).reshape(3,3)

print(f"\nMatriz original: \n {A}")

Transpuesta_A = A.T 

print(f"\nMatriz transpuesta: \n {Transpuesta_A}")

multiplicación_con_mismo_A = A * A

print(f"\nMatriz multiplicada elemento a elemento: \n {multiplicación_con_mismo_A}")

multiplicación_Alebraica_A = A @ A

print(f"\nMultiplicación Algebraica de A: \n {multiplicación_Alebraica_A}")

multiplicación_A_con_A_Transpuesta_matmul = np.matmul(A, A.T)
multiplicación_A_con_A_Transpuesta= A @ A.T

#Ambas funcionan igual ya que @ usa matmul por dentro
print(f"\nMultiplicación con Transpuesta con matmul: \n {multiplicación_A_con_A_Transpuesta_matmul}")
print(f"Multiplicación con Transpuesta con  @: \n {multiplicación_A_con_A_Transpuesta}")


B = np.array([[1,2,3],[4,5,6]])
print(f"\nB como matriz 2x3: \n {B}")

B_Array = B.flatten()
print(f"\nB_Array como Array: \n {B_Array}")

C = np.arange(1,13)

print(f"\nArray de 12 elementos: \n {C}")

C= C.reshape(3,4)

print(f"\nConversión a matriz 2x3(realmente es la vista): \n {C}")

C = np.arange(1,13)

print(f"\nArray de 12 elementos(aun se mantiene como array): \n {C}")