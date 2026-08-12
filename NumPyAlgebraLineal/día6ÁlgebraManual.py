import numpy as np

A = np.array([[1,2,3],[4,5,6]]) #2x3

B = np.array([[7,8],[9,10],[11,12]]) #3x2

#  1,2,3 | 7,8
#  4,5,6 | 9,10
#        | 11,12

def comprobación(A,B): 
  if( A.shape[1] == B.shape[0]):
    return True
  return False

def multplicación_manual(A, B): 
  if (comprobación(A,B)): 
   C = np.ones((A.shape[0], B.shape[1]))
   for i in range(A.shape[0]):
      for j in range(A.shape[0]):
        suma = 0
        for k in range(B.shape[0]):
         suma += A[i,k] * B[k,j]

        C[i,j] = suma
   return C
  raise ValueError("No puedes multiplicar Matrices con indices no compatibles.")

C_Dos = A @ B 
C = multplicación_manual(A,B)

print(f"\nMultiplicación Numpy: \n {C_Dos}")
print(f"\nMultiplicación Manual: \n {C}")

D = np.array([[1,2,3,4],[5,6,7,8]])  #2x4

E = np.array([[7,8,12],[9,10,43],[11,12,43]]) #3x3

try: 
  print(f"{multplicación_manual(D,E)}")
except ValueError as e: 
  print(f"\n{e}")