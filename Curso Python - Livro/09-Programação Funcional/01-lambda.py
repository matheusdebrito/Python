'''
Na prática são funções anônimas, que nem precisam ter um identificador definido. Em Python
podemos utiliza-las através do lambda.

❶ Criação de uma tupla de dicionários, com as compras a serem totalizadas
❷ A função map() retorna um iterator, e aqui convertemos em uma tupla para sua total
realização… Basicamente fazendo uma eager evaluation, isso é necessário por que
queremos percorre-la duas vezes no final, gerar uma lista (ou poderíamos imprimir a
tupla mesmo) e fazer um somatório
❸ Usamos a função map(), que recebe dois argumentos, uma function e um ou mais iterables.
Para cada iteração, é executada a função passando o(s) elemento(s) da iteração passados
como parâmetro
❹ Em vez de passar uma função já definida, podemos passar uma função anônima inline.
Neste caso o produto da quantidade e preço de cada compra.
❺ A tupla de totais é totalizada, usando a função sum() que itera em cada elemento
acumulando seu total
'''

compras = ( #❶
{'quantidade': 2, 'preco': 10},
{'quantidade': 3, 'preco': 20},
{'quantidade': 5, 'preco': 14},
)
totais = tuple( #❷
map( #❸
lambda compra: compra['quantidade'] * compra['preco'], #❹
compras
)
)
print('Preços totais:', list(totais))
print('Total geral:', sum(totais)) #❺