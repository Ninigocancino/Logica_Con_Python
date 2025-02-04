
#Instrucción en lenguaje natural: Declara una variable 'puntaje', asígnale un valor numérico de 85, luego verifica si la variable 'puntaje' es mayor o igual a 90. Si la condición es verdadera entonces imprime el mensaje 'Excelente', si la condición no se cumple entonces verifica que la variable 'puntaje' sea mayor o igual a 70. Si la condición es verdadera, entonces imprime el mensaje 'Bueno'. Si ninguna de las condiciones se cumple entonces imprime el mensaje 'Necesitas mejorar'

puntaje = 85
if puntaje >= 90:
    print('Excelente')
elif puntaje >= 70:
    print('Bueno')
else:
    print('necesitas mejorar')