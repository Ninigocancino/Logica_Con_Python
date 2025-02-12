
#Instrucción en lenguaje natural: Declara una variable llamada 'edad' guarda en ella un valor de 25, luego declara una segunda variable llamada 'tiene_licencia' y guarda un booleano 'True'. Verifica si 'edad' es mayor o igual a 18 y si 'tiene_licencia' es True entonces imprime en pantalla el mensaje "Puedes conducir", si la condición no se cumple verifica si 'edad' es mayor o igual a 18 y si no 'tiene_licencia' es True entonces imprime el mensaje 'Necesitas obtener una licencia para conducir'. Pero si ninguna de las condiciones se cumple, entonces imprime el mensaje "No puedes conducir"


edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad >= 18 and not tiene_licencia:
    print("Necesitas obtener una licencia para conducir")
else:
    print("No puedes conducir")