# Declara una lista llamada numeros que contenga los valores [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Luego, utiliza una lista de comprensión para crear una nueva lista llamada pares. En esta lista de comprensión, crea un ciclo que itera sobre cada elemento de la lista numeros, asigna el valor actual a la variable numero, y verifica si el valor de numero es divisible entre 2 (es decir, si es par). Si la condición es verdadera, el valor de numero se incluye en la lista pares. Finalmente, imprime en la consola el valor de pares.

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)