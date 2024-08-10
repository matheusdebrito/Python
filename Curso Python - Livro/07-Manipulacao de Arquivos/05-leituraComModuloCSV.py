import csv

with open('testeCSV.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print(f'Nome: {pessoa[0]} Idade: {pessoa[1]}')
        print('Nome: {} Idade: {}'.format(pessoa[0], pessoa[1]))