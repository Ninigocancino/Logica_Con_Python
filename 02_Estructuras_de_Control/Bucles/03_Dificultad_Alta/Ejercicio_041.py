#Instrucciones en lenguaje natural: Inicia un ciclo donde el iterador 'i' tome valores en un rango de 1 a 5, a la vez inicia un ciclo interno donde el iterador 'j' tome valores en un rango de 1 a 5. Si la suma de 'i' + 'j' es igual a 6, entonces imprime el símbolo '*' y disponlo de forma horizontal. En caso contrario imprime el símbolo '-'. Por ultimo imprime una línea vacía en cada ciclo principal.


for i in range(1, 6):
    for j in range(1, 6):
        if i + j == 6:
            print("*", end=" ")
        else:
            print("-", end=" ")
    print()