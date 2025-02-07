

#Instrucciones en lenguaje natural: Solicita al usuario que ingrese su edad, convierte el 'input' a un valor numérico de tipo entero y guárdalo en la variable 'edad'. Verifica si la variable 'edad' es mayor o igual a 18, si la condición se cumple; entonces imprime el mensaje 'Eres mayor de edad', si la condición anterior se cumple pero además 'edad' es mayor o igual 65, entonces imprime el mensaje 'y persona de la tercera edad'. Pero si la ultima condición no se cumple y solo se cumple la primera entonces imprime el mensaje 'y un adulto joven'. Pero si ninguna de las condiciones se cumple, entonces imprime el mensaje "Eres menor de edad'  


edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
    if edad >= 65:
        print(" y una persona de la tercera edad")
    else: 
        print("y un adulto joven")
else: 
    print("Eres menor de edad")