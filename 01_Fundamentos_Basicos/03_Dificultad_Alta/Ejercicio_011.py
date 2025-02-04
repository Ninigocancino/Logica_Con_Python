
#Enunciado: "Se solicita al usuario que ingrese un valor número que cambia de tipo 'string' a tipo 'float' y que se guarda en la variable 'n_1'. Luego, se pide al usuario que ingrese un 2do y 3er valor número que cambian de tipo 'string' a tipo 'float' y que se guardan en las variables 'n_2' y 'n_3' respectivamente. Luego se toman las variables 'n_1', 'n_2' y 'n_3', se suman y se divide en entre 3 y se guarda la operación en la variable 'promedio'.  Finalmente se imprime la variable promedio."

n_1 = float(input("Ingresa un número: "))
n_2 = float(input("Ingresa un segundo número: "))
n_3 = float(input("Ingresa un tercer número: "))
promedio = (n_1 + n_2 + n_3) / 3 
print(promedio)
