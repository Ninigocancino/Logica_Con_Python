

#Instrucción en lenguaje natural: Declara una variable llamada 'anio' y guarda en ella el valor numérico 2024.Verifica si el resto de la división de la variable variable 'anio'  entre 4 es 0 y el resto de la división de la variable 'anio' entre 100 es diferente de 0, ó bien el resto de la división de  'anio' entre 400 tiene como residuo 0. Si alguna de estas condiciones son verdaderas, entonces imprime el mensaje 'El año es bisiesto'. De lo contrario, imprime el mensaje 'El año no es bisiesto'

anio = 2025
#if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 ==0): #También funciona de  esta forma
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 ==0):
    print("El año es bisiesto")
else: 
    print("El año no es bisiesto")
