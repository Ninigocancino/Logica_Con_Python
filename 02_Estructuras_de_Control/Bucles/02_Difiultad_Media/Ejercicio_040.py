#Instrucción en lenguaje natural: Inicia un ciclo donde el iterador 'i' tome valores en un rango que va 1 a 5 a la vez inicia un ciclo interno donde el iterador 'j' tome valores en un rango que va de 1 al valor que toma 'i' + 1. Después imprime el valor que toma 'j' en cada iteración y disponlo de forma horizontal, al finalizar cada ciclo interno imprime una línea vacía para separar las iteraciones de 'i'

for i in range(1,6):
    for j in range(1, i +1 ):
        print(j, end=' ')
    print()
