'''
Um outro tipo que faz parte dos alicerces do Python são os dicionários (dict), comparado com
outras linguagens uma dicionário é similar a um HashMap, ou uma array associativa no PHP, e vai
muito além disso.
Um dicionário é algo similar a uma lista de chave e valor, mas sem ordenação, por que as chaves
são transformadas em hashs por questão de performance.
Assim como as listas, os dicionários não são tipados, nem a chave, nem o valor. Mas a chave precisa
ser de um tipo imutável (como str, int, float ou tuple) ou seja cada elemento pode ser de um tipo
diferente. Vamos a alguns exemplos.

❶ Lista dos membros (métodos, constantes, …) disponíveis para o tipo dict, uma dica é
utilizar a função help(dict) que detalhará melhor cada um deles
❷ A função len() pode ser utilizada com qualquer objeto, e ela retornar o seu tamanho, a
implementação específica depende de cada classe, no caso dos dicionários, será o número
de elementos (chave e valor)
❸ O uso do recurso de indexação também funciona nos dicionários usando a chave do valor
que se quer encontrar
❹ Ao tentar recuperar um valor de uma chave inexistente através do índice o Python gera
uma exceção do tipo KeyError
❺ O método keys() retorna uma espécie de lista (dict_keys) com todas as chaves
❻ O método values() retorna uma espécie de lista (dict_values) com todos os valores
❼ O método items() retorna uma espécie de lista (dict_items) com todos as chaves e valores,
em algo similar a uma lista de tuplas
❽ O método get() funciona de forma similar ao índice, porém caso a chave não exista
retorna um None. Também é possível colocar um segundo parâmetro com o valor a ser
retornado caso a chave não exista
'''

pessoa = {
    'nome': 'Juracy Filho',
    'idade': 43,
    'cursos': ['docker', 'python']
}
print(type(pessoa))

dir(dict)
print(len(pessoa)) #2
print(pessoa) #3
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa.keys()) #5
print(pessoa.values()) #6
print(pessoa.items()) #7
print(pessoa.get('idade')) #8
print(pessoa.get('tags'))
print(pessoa.get('tags', []))
