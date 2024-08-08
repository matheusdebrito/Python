"""
❶ É possível alterar o valor de uma determinada chave, se a chave não existir ela será criada
❷ O método pop() retorna o valor de uma determinada chave e a remove do dicionário
❸ O método update() recebe um outro dicionário e atualiza o objeto principal (merge)
❹ O del também permite remover elementos atráves da sua chave
❺ O método clear() limpa completamente o dicionário
"""

pessoa = {'nome': 'Juracy Filho', 'idade': 43, 'cursos': ['docker', 'python']}
print(pessoa)
pessoa['cursos'].append('angular')
print(pessoa)