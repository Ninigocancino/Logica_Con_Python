
#Instrucciones en lenguajes natural: Se inicia un bucle externo donde el iterador i toma valores en un rango de 1 a 5. Dentro de este bucle, se inicia un bucle interno donde el iterador j también toma valores en un rango de 1 a 5. En cada iteración del bucle interno, se imprime el resultado de la multiplicación de i y j, se dispone cada resultado de forma horizontal seguido de un espacio. Después de que se completa el bucle interno, se imprime una nueva línea para separar los resultados de cada iteración del bucle externo."

for i in range(1,6):
    for j in range(1,6):
        print(i * j, end=" ")
    print()