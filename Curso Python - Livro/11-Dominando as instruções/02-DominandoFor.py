'''
❶ Pular os números ímpares
❷ Caso o valor do d100 seja igual ao número da iteração atual… Bingo e encerra a iteração
❸ Caso não tenha ocorrido um break finaliza sem sucesso!
'''

from random import randint

def d100():
    """Dados de 100 lados"""
    return randint(0, 100)

for i in range(100):
    if i % 2 == 1: #1
        continue

    if d100() == i: #2
        print('Bingo', i)
        break
else: #3
    print('Não tivemos um vencedor')