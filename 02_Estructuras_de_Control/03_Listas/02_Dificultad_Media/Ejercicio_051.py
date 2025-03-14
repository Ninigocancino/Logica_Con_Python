# Declara una lista llamada numeros que contenga los valores [1, 2, 3, 4, 5]. Luego, utiliza una lista de comprensión para crear una nueva lista llamada cuadrados. En esta lista de comprensión, itera sobre cada elemento de la lista numeros, asignando el valor actual a la variable numero, y eleva al cuadrado. Almacena el resultado en la lista cuadrados. Finalmente, se imprime en la consola el valor de cuadrados.


numeros = [1,2,3,4,5]
cuadrados = [numero ** 2 for numero in  numeros]
print(cuadrados)