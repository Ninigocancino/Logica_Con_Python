
"""
Instrucciones en lenguaje natural: "Declara una variable llamada temperatura y asignale el valor numérico 30. Luego, verifica si el valor de temperatura es mayor que 25. Si la condición es verdadera, imprime en la consola el mensaje 'Hace calor'. Si no se cumple esa condición, verifica si el valor de temperatura es menor que 10. Si esta segunda condición es verdadera, imprime en la consola el mensaje 'Hace frío'. Si ninguna de las condiciones anteriores es verdadera, imprime en la consola el mensaje 'Clima agradable'."
"""

temperatura = 30
if temperatura > 25:
    print("Hace calor")
elif temperatura < 10:
    print("Hace frío")
else:
    print("Clima agradable")