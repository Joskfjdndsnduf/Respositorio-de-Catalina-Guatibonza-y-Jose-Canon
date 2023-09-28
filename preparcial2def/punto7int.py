import numpy as np

def crearmatriz(n):
    M=np.zeros((n+1,n+1))
    for i in range(n+1):
        for j in range(n+1):
            if 1-(i*1/n)**2-(j*1/n)**2>=0:
                M[i][j]=np.sqrt(1-(i*1/n)**2-(j*1/n)**2)
            else:
                M[i][j]=0
        
    return M


def promedios(mat,n):
    suma_total = 0
    filas = len(mat)
    columnas = len(mat[0])
    
    for i in range(filas - 1): 
        for j in range(columnas - 1): 
            cuadrado = [
                mat[i][j], mat[i][j+1],
                mat[i+1][j], mat[i+1][j+1]
            ]
            suma_cuadrado = sum(cuadrado)
            suma_total += suma_cuadrado/n**2
    
    return suma_total

def integral(n):
    m=crearmatriz(n)
    return promedios(m,n)

print(integral(9))