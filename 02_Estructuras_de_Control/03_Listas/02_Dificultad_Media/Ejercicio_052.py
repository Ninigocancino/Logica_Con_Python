# Se declara una lista llamada palabras que contiene los valores ['hola', 'mundo', 'python']. Luego, se utiliza una lista de comprensión para crear una nueva lista llamada longitudes. En esta lista de comprensión, se itera sobre cada elemento de la lista palabras, asignando el valor actual a la variable palabra, y se calcula la longitud de cada palabra usando la función len(). El resultado se almacena en la lista longitudes. Finalmente, se imprime en la consola el valor de longitudes.

palabras = ['hola','mundo','python']
longitudes = [len(palabra) for palabra in palabras]
print(longitudes)