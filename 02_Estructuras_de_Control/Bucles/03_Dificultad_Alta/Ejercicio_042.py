#Así daría las instrucciones en lenguaje natural a Python
#Por cada valor de i en el rango de 1 a 5, y por cada valor de j en el rango de 1 a 5, si la suma de i y j es igual a 6, imprime "*" seguido de un espacio. En caso contrario, imprime un espacio doble. Al final de cada ciclo interno (j), se imprime un salto de línea (print()).

for i in range(1, 6):
    for j in range(1, 6):
        if i == j or i + j == 6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()