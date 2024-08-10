"""
❶ O open() suporta um segundo parâmetro para indicar o modo de abertura do arquivo, o
default é 'r' que é para leitura, aqui usamos o 'w' para abri-lo para gravação. Outra opção
é abri-lo em modo binário ('rb' e 'wb'), essencial para arquivos como imagens, vídeos,
áudios, etc
"""

with open('testeCSV.csv') as entrada:
    with open('pessoas.txt', 'w') as saida: #❶
        for registro in entrada:
            pessoa = registro.strip().split(',')
            print('Nome: {} Idade: {}'.format(*pessoa), file=saida)