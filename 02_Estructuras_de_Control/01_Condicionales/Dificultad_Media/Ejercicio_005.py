
#Instrucciones en lenguaje natural: Declara una variable llamada 'edad', luego guarda en ella un valor numérico de 15. Verifica si la variable edad es menor a 13, si condición es verdadera entonces imprime el mensaje 'Eres un niño', si la condición anterior no se cumple verifica que la variable es edad es menor a 18, si la condición es verdadera, entonces imprime el mensaje 'Eres un adolescente'. Pero si ninguna de las condiciones anteriores se cumple, entonces imprime el mensaje 'Eres un adulto'

edad = 15
if edad < 13:
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolescente")
else:
    print('Eres un adulto')