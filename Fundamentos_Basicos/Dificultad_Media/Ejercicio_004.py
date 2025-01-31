
#Enunciado: "Se pide al usuario que ingrese un valor número al cual se cambia su tipo de dato de 'string' a 'entero' para luego ser guardado en la variable 'lado_1'. Luego se pide al usuario que ingrese un valor número al cual se cambia su tipo de dato de 'string' a 'entero' para luego ser guardado en la variable 'lado_2'. Luego se pide al usuario que ingrese un nuevo valor número  al cual se cambia su tipo de dato de 'string' a 'entero' para luego ser guardado en la variable 'altura'. Luego se declara la variable 'formula' que toma la variable 'lado_1' para multiplicarla por la variable 'lado_2' y la variable 'altura'. por último se imprime la variable 'formula' "

lado_1 = int(input("Ingresa un número entero: "))
lado_2 = int(input("Ingresa un nuevo número entero: "))
altura = int(input("Ingresa un último número entero: "))
formula = lado_1 * lado_2 * altura
print(formula)