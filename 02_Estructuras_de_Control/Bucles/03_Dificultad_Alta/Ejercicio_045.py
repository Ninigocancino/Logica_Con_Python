#inicia un bucle externo donde el iterador i tome valores en un rango de 1 a 5. Dentro de este bucle, inicia un bucle interno donde el iterador j también tome valores en un rango de 1 a 5. En cada iteración del bucle interno, verifica si i es igual a j, si la suma de i y j es igual a 6, si i es igual a 1, si j es igual a 1, si i es igual a 5 o si j es igual a 5. Si alguna de estas condiciones es verdadera, imprime un asterisco (*), seguido de un espacio. Si ninguna de las condiciones es verdadera, imprime un espacio, seguido de otro espacio. Después de que se completa el bucle interno, se imprime una nueva línea para separar los resultados de cada iteración del bucle externo.

for i in range(1, 6):
    for j in range(1, 6):
        if i == j or i + j == 6 or i == 1 or j == 1 or i == 5 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()