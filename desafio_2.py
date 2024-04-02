
valor = int(input('Digite um valor para verificar se pertence à sequência de Fibonacci: '))
lista_inicial = [0, 1]
pertence = False
for i in range(2, valor):
    lista_inicial.append(lista_inicial[i-1] + lista_inicial[i-2])
    if lista_inicial[i] == valor:
        pertence = True
        break
    elif lista_inicial[i] > valor:
        break

if pertence:
    print(f'O valor {valor} pertence à sequência de Fibonacci')
else:
    print(f'O valor {valor} não pertence à sequência de Fibonacci')
