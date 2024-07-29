'''
❶ O recurso de acesso aos elementos da lista aceita um segundo parâmetro separado por :,
com isso ele retornará uma nova lista, começando a partir do elemento indicado até o
elemento anterior ao segundo parâmetro
❷ Podemos também utilizar índices negativos, neste caso retorna uma nova lista a partir do
segundo elemento até o penúltimo
❸ Deixando o segundo parâmetro em branco significa até o final (incluindo o último)
❹ O primeiro parâmetro em branco equivale a 0, ou seja, primeiro elemento
❺ Retorna uma nova lista com todos os elementos da original, útil para executar cópias de
uma lista
❻ Um terceiro parâmetro pode ser informado como step, o default é 1, neste caso depois de
pega o primeiro elemento ele pulará dois (em vez de um) e assim seguirá até o fim da faixa
❼ É possível também informar um step negativo, indicando que a nova lista começará a
partir do último elemento da faixa até o primeiro, pulando de um em um (poderia ser
outro número também)
❽ A instrução del permite a remoção de elementos de uma lista através do seu índice ou
fatiamento
'''

lista = [1, 5, 'Juracy', 'Leonardo', 3.1415]
print(lista[1:3])
del lista[2] # Deleta o item no índice 2
print(lista)
