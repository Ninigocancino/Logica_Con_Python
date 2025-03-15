# Declara una lista llamada palabras que contenga los valores ['python', 'es', 'un', 'lenguaje', 'poderoso']. Luego, declara una variable llamada longitud_minima y asignale el valor 3. A continuación, utiliza una lista de comprensión para crear una nueva lista llamada filtradas. En esta lista de comprensión, crea un ciclo que itere sobre cada elemento de la lista palabras, asignando el valor actual a la variable palabra, y verifica si la longitud de palabra es mayor o igual que el valor de longitud_minima. Si la condición es verdadera, incluye el valor de palabra en la lista filtradas. Finalmente, se imprime en la consola el valor de filtradas.


palabras = ['python', 'es', 'un', 'lenguaje', 'poderoso']
longitud_minima = 3
filtradas = [palabra for palabra in palabras if len(palabra)>= longitud_minima]
print(filtradas)