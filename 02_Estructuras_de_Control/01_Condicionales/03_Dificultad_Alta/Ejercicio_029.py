

#Instrucciones en lenguaje natural: Declara una variable llamada 'numero' dale un valor de 15. Verifica si numero es mayor que 10 y si el residuo de la división de numero entre 2 es 0, si la condición es verdadera entonces imprime el mensaje 'El número es mayor que 10 y es par'. Si la condición no se cumple entonces verifica si numero es mayor que 10 y que al dividir numero entre 2 el residuo no sea 0, si la condición se cumple entonces imprime el mensaje 'El número es mayor que 10 y es impar'. De no cumplirse la condición anterior verifica si numero es menor o igual que 10 y que numero dividido entre 2 no tenga residuo, si la condición se cumple entonces imprime el mensaje 'El número es menor o igual a 10 y es par. Pero si ninguna de las condiciones se cumple, entonces imprime el mensaje "El número es menor o igual a 10 y es impar'

numero = 15
if numero > 10 and numero % 2 == 0:
    print("El número es mayor que 10 y es par")
elif numero > 10 and numero % 2 != 0:
    print("El número es mayor que 10 y es impar")
elif numero <= 10 and numero % 2 == 0:
    print("El número es menor o igual a 10 y es par")
else:
    print("El número es menor o igual a 10 y es impar")