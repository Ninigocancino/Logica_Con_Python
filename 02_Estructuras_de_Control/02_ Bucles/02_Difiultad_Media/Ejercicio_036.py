#Declara una variable llamada 'suma' asígnale el valor de 0, luego inicia un ciclo donde el iterador 'i' inicie una secuencia en un rango que va de 1 a 6. Luego al valor de suma incrementa el valor de 'i' en cada iteración. Por último imprime el mensaje "La suma total es: " y concatena el valor de final de la variable 'suma' 

suma = 0
for i in range(1,6):
    suma += i
print("La suma total es:", suma)