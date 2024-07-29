'''
❶ O método index retorna o índice de um elemento indicado
❷ Executar o método index com um valor não pertencente a lista retornará um ValueError
❸ O operador in retorna se um objeto está contido na lista
❹ Ao tentar acessar um índice inexistente na lista, normalmente maior que o número de
elementos, o Python levanta uma exceção do tipo IndexError
❺ É possível acessar elementos através de uma indexação negativa, sendo o último elemento
-1, o penúltimo -2 e assim por diante
'''

lista = [1, 5, 'Juracy', 'Leonardo', 3.1415]
print(lista.index('Juracy')) #Retorna a posição de 'Juracy'

x = 'Matheus' in lista # Retorna true se 'Matheus' estiver na lista ou false se não estiver
print(x)

y = lista[0] # pega o item na posição 0 da lista
print(y)