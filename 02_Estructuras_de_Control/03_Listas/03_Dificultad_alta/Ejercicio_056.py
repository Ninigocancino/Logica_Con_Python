# Crea una lista llamada matriz que contiene tres listas internas: [1, 2, 3], [4, 5, 6] y [7, 8, 9].Crea una nueva lista llamada transpuesta utilizando una lista de comprensión anidada. En la lista de comprensión externa, itera sobre los índices de las columnas de la matriz (desde 0 hasta la longitud de la primera fila).En la lista de comprensión interna, itera sobre cada fila de la matriz y toma el elemento en la posición i de cada fila.Guarda cada columna generada en la lista transpuesta.Finalmente, imprime la lista transpuesta.

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print(transpuesta)