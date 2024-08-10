"""
❶ A função open() do __builtins__ (que é um atalho para o io.open()), abre o arquivo
passado como argumento e retorna uma instância do io.TextIOWrapper
❷ O método read() lê todo o conteúdo do arquivo
❸ O método close() fecha o arquivo
"""

arquivo = open('teste.txt') #1
dados = arquivo.read() #2
arquivo.close() #3

for registro in dados.splitlines():
    print(registro.split(','))

arquivo2 = open('teste2.txt')

for registro2 in arquivo2:
    print(registro2)

arquivo2.close()

