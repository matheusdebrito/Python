"""
❶ A função open() do __builtins__ (que é um atalho para o io.open()), abre o arquivo
passado como argumento e retorna uma instância do io.TextIOWrapper
❷ O método read() lê todo o conteúdo do arquivo
❸ O método close() fecha o arquivo
"""

arquivo = open('testeCSV.csv') #1
dados = arquivo.read() #2
arquivo.close() #3

lista = []

for i in dados.splitlines():
    lista.append((i.split(',')[0]))
    lista.append((i.split(',')[1]))
print(lista)