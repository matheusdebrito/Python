'''
As tuplas são similares a lista porém elas são imutáveis, e portanto não podem receber alterações.
Existem algumas situações em que uma tupla pode ser preferida a uma lista, uma delas é como
chave em um dicionário, como veremos na seção Dicionários.

❶ Tupla vazia, a partir da chamada da classe tuple
❷ Tupla vazia, representada por um ()
❸ Diferente das listas, as tuplas possuem poucos métodos, e estes funcionam de forma
similar às listas
❹  Erro muito comum, em Python esta expressão utilizando parenteses é tratada apenas
como precedência, o que acaba atribuindo apenas a string 'um' a variável
❺ Sintaxe correta para uma tupla de um elemento
❻ Indexação similar as listas
❼ Fatiamento similar as listas
'''
tupla = tuple() #1
tupla = () #2
print(type(tupla))
tupla = ('um') #4
print(type(tupla))
tupla = ('um',) #5
print(type(tupla))
print(tupla[0]) #6

cores = ('verde', 'amarelo', 'azul', 'branco')
print(cores[0])
print(cores[-1])
print(cores[1:])
print(cores[0:2])
