
#Instrucción en lenguaje natural: Declara una variable llamada 'numeros' y asígnale como valor una lista que contenga los numero '1,2,3,4,5'. Luego inicia un ciclo donde la variable numero sea el iterador que recorre cada elemento en la variable 'numeros', luego verifica en cada iteración si el residuo del iterador dividido entre 2 es igual a 0, si la condición se cumple entonces imprime el valor de 'numero' y concatena el mensaje 'es par'. Si la condición no se cumple entonces imprime el valor de 'numero' y concatena el mensaje 'es impar'

numeros = [1,2,3,4,5]

for numero in numeros:
    if numero % 2 ==0:
        print(numero, "Es par")
    else:
        print(numero, "Es impar")