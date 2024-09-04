'''
❶ A função randint() do módulo random, gera um número randômico na faixa indicada
❷ Avalia se o número é impar
❸ Instrução continue pula toda a lógica do bloco e a condição do laço é reavaliada. (Volta o laço para o início)
❹ Instrução break encerra imediatamente o laço, não executando a cláusula else caso exista
❺ A cláusula else do while é executada apenas se não ocorrer um break
'''

from random import randint 

numeros = []

while len(numeros) < 10:
    numero = randint(1, 20) #1

    if numero % 2 == 1: #2
        print(f"{numero} é ímpar") 
        continue #3

    print(f'{numero} adicionado ao conjunto')
    numeros.append(numero) 

    if numero == len(numeros):
        print('BINGO', numeros)
        break #4
else:
    print(numeros) #5