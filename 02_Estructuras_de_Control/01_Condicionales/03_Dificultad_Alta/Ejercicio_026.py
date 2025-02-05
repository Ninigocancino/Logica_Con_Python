
#Instrucciones en lenguaje natural: Declara una variable llamada 'numero', asígnale el valor numérico 12. Después verifica si la variable numero al dividirse entre 3 tiene por residuo 0 y si numero al dividirse entre cuatro tiene como residuo 0, si la condición es verdadera entonces imprime el valor 'El número es divisible entre 3 y 4'. Si la condición anterior no se cumple entonces verifica si la variable numero al dividirse entre 3 tiene como residuo 0, si la condición  es verdadera, entonces imprime el mensaje 'El número es divisible entre 3'.Si las condiciones anteriores no se cumplen verifica si la variable numero dividida entre 4 tiene por residuo 0, si la condición es verdadera, entonces imprime el mensaje 'El número es divisibles entre 4'. Pero si  ninguna de las condiciones de cumple, entonces imprime el mensaje 'El número no es divisible entre 3 ni 4'


numero = 12
if numero % 3 == 0 and numero % 4 == 0:
    print("El número es divisible entre 3 y 4")
elif numero % 3 == 0:
    print("El número es divisible entre 3")
elif numero % 4 == 0:
    print("El número es divisible entre 4")
else:
    print("El número no es divisible entre 3 ni 4")