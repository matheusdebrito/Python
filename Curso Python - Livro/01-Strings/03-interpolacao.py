from string import Template #1

""""
❶ Importação do classe Template do módulo string
❷ Interpolação com o operador módulo % (legado)
❸ Interpolação com a função str.format(), método preferencial até o Python 3.5, tendo
ainda vários usos como na internacionalização e sempre que a avaliação precise ser
adiada.
❹ O novo padrão de interpolação, chamado também de f-string, só está disponível a partir do
Python 3.6 e sempre processa a string imediatamente (eager evaluation)
❺ Formato de interpolação muito usado para tratar com segurança dados entrados pelo
usuário
"""

nome, idade = 'Ana', 30
print('Nome: %s Idade: %d' %(nome, idade)) #2
print('Nome: {0} Idade: {1}'.format(nome, idade)) #3
print(f'Nome: {nome} Idade: {idade}') #4

s = Template('Nome: $nome Idade: $idade') #5
print(s.substitute(nome=nome, idade=idade)) #6

