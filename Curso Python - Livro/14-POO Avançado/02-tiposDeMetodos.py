'''
Existem 3 tipos de métodos:
• De instância
• De classe
• Estático
Até agora todos os métodos que criamos foram de instância, recebem no primeiro parâmetro a
instância que disparou o método, é possível chama-lo a partir da classe mas isso exigiria passar
explicitamente o self: EvolucaoHumana.das_cavernas(pedro).
O método de classe utiliza o decorator classmethod na sua sintaxe, com isso o método passar a estar
associado diretamente a classe e não a instância, porém ainda pode ser chamada a partir de um
objeto. Seu primeiro parâmetro é a classe que disparou o método (que pode ser usado para
polimorfismo de várias maneiras), que foi convencionado com o nome de cls.
O método estático é mais simples, utiliza o decorator staticmethod e não recebe parâmetro nenhum,
pode ser chamado tanto da classe quanto da instância. Em termos práticos nada mais é do que uma
função no namespace da classe.
---------------------------------------------------------------------------------------------------
1 Decorator para métodos estáticos (__builtins__)
2 Decorator para métodos de classe (__builtins__)
3 Método de classe que recebe pelo menos o parâmetro da classe que disparou o método, o
que permite algum polimorfismo
4 Chamada de método estático (com diversas origens diferentes)
5 Chamada de método de classe (com diversas origens diferentes)

'''

class EvolucaoHumana(object):
    especie = ''

    @staticmethod #1
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)
    
    @classmethod #2
    def is_evoluido(cls): #3
        return cls.especie == cls.especies()[-1]
    
    def __init__(self, nome):
        self.nome = nome

class Neanderthal(EvolucaoHumana):
    especie = EvolucaoHumana.especies()[-2] #4


class HomoSapiens(EvolucaoHumana):
    especie = EvolucaoHumana.especies()[-1] #4

if __name__ == '__main__':
    jose = HomoSapiens('José')
    grokn = Neanderthal('Grokn')

    print(f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}') #4
    print(f'Evolução (a partir da instancia): {", ".join(jose.especies())}') #4
    print(f'Homo Sapiens evoluído? {HomoSapiens.is_evoluido()}') #5
    print(f'Neanderthal evoluído? {Neanderthal.is_evoluido()}') #5
    print(f'José evoluído? {jose.is_evoluido()}') #5
    print(f'Grokn evoluído? {grokn.is_evoluido()}') #5
