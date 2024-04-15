#Taller Numpy
#arreglos n-dimensionales
import numpy as np

#Crear un ndarray de 2 dimensiones a partir de una lista
A = np.array ([[1,5],[7,9]])
B = np.array ([[2,0],[1,3]])

#Producto punto entre ndarrays
C = np.dot(A,B)
print(C)


#Solucion de un sistema de ecuaciones con numpy
m_solucion=np.array([5,17])
m= np.linal.solve(A,m_solucion)
print(m)