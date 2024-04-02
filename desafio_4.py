import time
import random
from typing import List
from typing import Dict
# O dicionário abaixo representa as lampadas e seus estados. O primeiro valor representa se a lampada está acesa ou apagada, e o segundo valor representa se a lampada está se a lampada está quente ou fria
dicionario_lampadas : Dict[str, List[bool]] = {
    'lampada_1': [False, False], #[estado, temperatura]
    'lampada_2': [False, False], #[estado, temperatura] 
    'lampada_3': [False, False] # [estado, temperatura]
}

abertura_de_salas : int = 2 #Numero de tentativas de aberura de salas

def acender_lampada(estado: list) -> list:
    estado[0] = True
    estado[1] = True
    return estado

def apagar_lampada(lampada: list) -> list:
    lampada[0] = False
    return lampada

#Algoritmo de identificação de lampadas


def identificar_lampada(lampada_teste_1 : str, lampada_teste_2 : str):

    # Agora, vamos acender a primeira lampada e apaga-la após 5 segundos. Em seguida, acender a segunda lampada.
    dicionario_lampadas[lampada_teste_1] = acender_lampada(dicionario_lampadas[lampada_teste_1])

    #Espera de 5 segundos
    time.sleep(5)
    dicionario_lampadas[lampada_teste_1] = apagar_lampada(dicionario_lampadas[lampada_teste_1])
    dicionario_lampadas[lampada_teste_2] = acender_lampada(dicionario_lampadas[lampada_teste_2])

    #Em teoria, a primeira lampada acesa estaria quente, mas apagada. Enquanto que a segunda lampada acesa estaria quente e acesa.

    #Agora, vamos identificar as lampadas que correspondem aos interruptores A e B e C
    interruptor_a : str = ""
    interruptor_b : str  = ""
    interruptor_c  : str = ""

    lista_aletaoria : List[int] = [1, 2, 3]

    for _ in range(abertura_de_salas): #Para cada sala aberta, vamos identificar uma lampada (2 tentativas)

        n : int = random.choice(lista_aletaoria) # Ao abrir uma sala, escolhemos uma lampada aleatória para identificar o interruptor

        if dicionario_lampadas[f'lampada_{n}'][0] == True:
            interruptor_b = f"lampada_{n}"
        elif dicionario_lampadas[f'lampada_{n}'][1] == True:
            interruptor_a = f"lampada_{n}"
        else:
            interruptor_c = f"lampada_{n}"
            
        lista_aletaoria.remove(n)
    print(f"Interruptor A: {interruptor_a}")
    print(f"Interruptor B: {interruptor_b}")
    print(f"Interruptor C: {interruptor_c}")    
    # o resultado abaixo identificara duas lampadas, logo, a terceira lampada corresponderá ao interruptor que sobrou


#=======================================================================================================
 # INICIO DO PROGRAMA   
#=======================================================================================================    
    

#Primeiro, vamos determinar duas lampadas para corresponder ao interruptor A e B, respectivamente 
numeros_aleatorios : List[int] = [1, 2, 3]

n1 : int = random.choice(numeros_aleatorios)
numeros_aleatorios.remove(n1)
n2 : int = random.choice(numeros_aleatorios)

identificar_lampada(f"lampada_{n1}", f"lampada_{n2}")