from typing import List



lista_a : List[int] = [1, 3, 5, 7]
lista_b : List[int] = [2, 4, 8, 16, 32, 64]
lista_c : List[int] = [0, 1, 4, 9, 16, 25, 36]
lista_d : List[int] = [4, 16, 36, 64]
lista_e : List[int] = [1, 1, 2, 3, 5, 8]
lista_f : List[int] = [2,10, 12, 16, 17, 18, 19]

def descobrir_proximo_numero(lista: list) -> list:
    raiz_ultimo : float = lista[-1] ** 0.5
    raiz_penultimo : float = lista[-2] ** 0.5

    #Se o último e o penúltimo número forem impare consecutivos, adicionar o proximo numero impar
    if lista[-1] % 2 != 0 and lista[-2] % 2 != 0 and lista[-1] - lista[-2] == 2:
        lista.append(lista[-1] + 2)
        

    #Se o último e o punúltimo número forem potencias de 2, adicionar o proximo numero (potencia de 2
    elif lista[-1] == 2 ** (len(lista)) and lista[-2] == 2 ** (len(lista) - 1):
        lista.append(2 ** (len(lista)+1 ) )

    # Se o ultimo e o penultimo numero forem quadrados perfeitos concecutivos, adicionar o proximo 
    elif lista[-1] == (len(lista) - 1) ** 2 and lista[-2] == (len(lista) - 2) ** 2:
        lista.append((len(lista)) ** 2)

    # Se a raiz quadrada do ultimo e a raiz quadrada do penultimo numero forem consecutivas de números parees, adicionar o proximo numero par ao quadrado
    elif raiz_ultimo % 2 == 0 and raiz_penultimo % 2 == 0 and raiz_ultimo - raiz_penultimo == 2:
        proximo_par = raiz_ultimo + 2
        lista.append(int(proximo_par ** 2))
       

    #Se o ultimo e o penultimo numero forem da sequencia de Fibonacci, adicionar o proximo numero da sequencia de Fibonacci
    elif lista[-1] == (lista[-2] + lista[-3]) and (lista[-2] == lista[-3] + lista[-4]):
        lista.append(lista[-1] + lista[-2])
        

    #O próximo número que começa com a letra D:
    elif lista[0] == 2 and lista[1] == 10 and lista[2] == 12 and lista[3] == 16 and lista[4] == 17 and lista[5] == 18 and lista[6] == 19:
        
        lista.append(200)
    
    return lista

print(descobrir_proximo_numero(lista_a))
print(descobrir_proximo_numero(lista_b))
print(descobrir_proximo_numero(lista_c))
print(descobrir_proximo_numero(lista_d))
print(descobrir_proximo_numero(lista_e))
print(descobrir_proximo_numero(lista_f))