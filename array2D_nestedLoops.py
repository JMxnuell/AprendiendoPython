
m = [ [1,7],
      [2,4],
    ]

n = [ [3,3],
      [5,2],
    ]

#MULTIPLICACION DE MATRICES
#Fila resultante lo define la fila de m
#Columna resultante lo define la columna de n
w = [[] for u in range(len(m))]
for z in w:
    for a in range(len(n[0])):
        z.append(0)

if len(m[0]) == len(n): # si la columna de m es igual a la fila de n se puede
    for i in range(len(m)): #fila nueva matriz
        for j in range(len(m[0])): #columna nueva matriz
            for k in range(len(n)): #filas de n
                w[i][j] += m[i][k] * n[k][j]
print(w)








