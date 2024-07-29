'''
❶ Strings suportam indexação e fatiamento, nestes casos se comportam como uma lista de
caracteres, mas detalhes em Exercício 11 - Indexação das Listas e Exercício 12 - Fatiamento
de Listas
❷ O operador in avalia se a primeira string está contida na segunda, retornando um
booleano
❸ A função len() pode ser utilizada com qualquer objeto, e ela retorna o seu tamanho, a
implementação específica depende de cada classe, no caso das strings, será o número de
caracteres
❹ O método lower() retorna uma nova string com todos os caracteres em minúsculo
❺ O método upper() retorna uma nova string com todos os caracteres em maiúsculo
❻ O método split() retorna uma nova lista de strings, cada elemento contendo uma palavra
da string original
'''

nome = 'Juracy Filho'
print(nome[:6])

print('re' in nome)

print(len(nome))

print(nome.lower())

print(nome.upper())

print(nome.split())