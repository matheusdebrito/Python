'''
❶ Veremos classes com mais detalhes em Programação orientada a objetos
❷ Documentação da classe: __doc__
❸ Constructor da classe, que recebe a potência
❹ Implementação do método especial __call__() indica que o objeto poderá ser chamado
como uma função
❺ Os objetos resultantes funcionarão como funções com uma closure (já que retem o estado
da construção da classe)
'''

class ClosureClass(object): #1
    """Calcula uma potência""" #2
 
    def __init__(self, potencia): #3
        self.potencia = potencia

    def __call__(self, valor): #4
        return valor ** self.potencia
    

quadrado = ClosureClass(2) #5
cubo = ClosureClass(3)

if callable(quadrado):
    print("quadrado: Objetos desta classe podem atuar como função")

print(f'Documentação: {ClosureClass.__doc__}')
print(f'3² => {quadrado(3)}')
print(f'5³ => {cubo(5)}')