#Declara una lista llamada numeros que contiene los valores [10, 20, 30, 40, 50]. Luego, utiliza una lista de comprensión para crear una nueva lista llamada incrementados. En esta lista de comprensión, itera sobre cada elemento de la lista numeros, asignando el valor actual a la variable numero, y suma 5 al valor de numero. Incluye el resultado en la lista incrementados. Finalmente, imprime en la consola el valor de incrementados.

numeros = [10,20,30,40,50]
incremnetados = [numero + 5 for numero in numeros]
print(incremnetados)