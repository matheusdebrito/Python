'''
Um dos tipos mais versáteis em Python são as listas (list), comparado com outras linguagens uma
lista é similar a uma array, porém ela vai muito além disso. As listas não são tipadas, ou seja cada
elemento pode ser de um tipo diferente, além disso existe o conceito de slicing que permite formas
extremamente poderosas de acesso aos seus elementos. Vamos a alguns exemplos.

❶ Lista dos membros (métodos, constantes, …) disponíveis para o tipo list, uma dica é
utilizar a função help(list) que detalhará melhor cada um deles
❷ A função len() pode ser utilizada com qualquer objeto, e ela retorna o seu tamanho, a
implementação específica depende de cada classe, no caso das listas, será o número de
elementos
❸ O método append() inclui um novo elemento na lista
❹ O uso do operador + com duas listas irá retorna uma nova lista juntando o conteúdo da
primeira com a segunda (sem alterar nenhuma delas)
❺ O método insert() inclui um novo elemento em uma posição específica da lista,
lembrando que a primeira posição começa em 0
❻ O método remove() retira um elemento da lista baseado no seu conteúdo, e não no seu
índice
'''
lista = []
lista.append(1)
lista.append(5)
print(lista)
print(len(lista))
print('-----------------------------------------------')
nova_lista = lista + ['Juracy', 'Leonardo', 3.1415]
print(nova_lista)
nova_lista.insert(0, 'Zero') #Insere 'Zero' na posição 0
print(nova_lista)
nova_lista.remove(5) #remove o item 5
print(nova_lista)