a = 2
b = '2'

print(type(a))
print(type(b))

print(a + int(b))
print(str(a) + b)

'''
A partir da versão 3, a divisão mesmo entre números inteiros sempre retorna um float
(ponto flutuante)
O operador // realiza a divisão de números e sempre retorna um int, truncando se
necessário
Em operações numéricas, objetos do tipo bool, retornam 1 para True e 0 para False
Fora a divisão, outras operações entre dois números podem retornar int ou float,
conforme o caso
'''
print('----------------------------------------')
print(10 /2 )
print(type(10/2))