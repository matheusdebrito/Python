'''
1 Atributos setados dentro da classe diretamente (e não nos métodos), são membros de
classe, e estão disponíveis diretamente através da classe e em todas as suas instâncias, a
não ser que exista um membro de instância de mesmo nome
2 Ao setar um atributo através do objeto/instância (self), o que criaremos será um membro
de instância
3 Ao acessar um atributo em uma instância e a mesma não possui-la, uma busca é feita em
sua classe (incluindo toda a herança)
4 Alterando o valor de um membro de classe “afeta” todas as instâncias da mesma
'''

class EvolucaoHumana(object):
    especie = 'Homo Sapiens' #1

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neaderthalensis' #2

if __name__ == '__main__':
    jose = EvolucaoHumana('José')
    grokn = EvolucaoHumana('Grokn')
    grokn.das_cavernas()


    print(f'EvolucaoHumana.especie: {EvolucaoHumana.especie}')
    print(f'jose.especie: {jose.especie}') #3
    print(f'grokn.especie: {grokn.especie}')

    EvolucaoHumana.especie = 'Homo Sapiens Sapiens' #4
    print(f'EvolucaoHumana.especie: {EvolucaoHumana.especie}')
    print(f'jose.especie: {jose.especie}')
    print(f'grokn.especie: {grokn.especie}')