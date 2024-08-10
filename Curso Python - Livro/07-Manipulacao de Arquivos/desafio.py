import csv

"""
Extrair o nono e o quarto campos do arquivo CSV sobre Região de influência das Cidades do IBGE.

O arquivo se encontra em ISO-8859-1 (aka latin1), será necessário usar o parâmetro encoding da função open.
"""

contador = 0

with open('dadosIBGE.csv', encoding='UTF-8') as entrada:
    for dado in csv.reader(entrada):
        print(f'9° Dado: {dado[8]}, 4° Dado: {dado[3]}')
        contador += 1
        if contador >= 10:
            break