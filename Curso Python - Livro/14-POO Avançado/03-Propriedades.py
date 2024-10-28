'''
❶ Criação do atributo “privado” para ser usado pela propriedade idade
❷ Getter
❸ Setter
❹ Validação, apenas número positivos são aceitos como idade
❺ Chamando o setter
❻ Chamando o getter
'''

class EvolucaoHumana(object):
    def __init__(self, nome):
        self.nome = nome
        self._idade = None #1

    def get_idade(self): #2
        return self._idade
    
    def set_idade(self, idade):
        if idade < 0: #4
            raise ValueError('Idade deve ser um número positivo')
        self._idade = idade

if __name__ == "__main__":
    jose = EvolucaoHumana('José')
    jose.set_idade(40) #5
    print(f'Nome: {jose.nome} Idade: {jose.get_idade()}') #6