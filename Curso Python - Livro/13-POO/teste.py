'''
❶ A instrução class é usada para definir uma classe, por convenção as classes definidas
além da biblioteca padrão devem usar camel case, neste caso Task
❷ Podemos definir de que outra classe iremos herdar, a classe mais básica é object, porém a
partir do Python 3 não precisamos definir a classe base caso a mesma seja object. Esta
linha poderia ser: class Task:
❸ Uma função dentro de uma classe, é chamada de método, e terá pelo menos um parâmetro
(o primeiro) que receberá o objeto instanciado que disparou a execução, isso é automático,
o usuário da classe só passará argumentos a partir do segundo parâmetro. Por convenção
este primeiro parâmetro é nomeado como self
❹ O método __init__() é disparado logo após a instanciação do objeto, seria algo equivalente
a um construtor
❺ Atribuições de membros em self, inicializa atributos da instância
❻ O método __str__() é chamado ao tentar converter o objeto em string, ou tentar imprimilo
por exemplo (que faz implícitamente essa conversão)
❼ A forma de instanciar um objeto de uma classe é chamar a classe de maneira análoga a
uma função, passando argumentos se necessário
❽ O método task.done() altera o atributo de instância feito para True
'''

from datetime import datetime

class Task(object): #1 2
    def __init__(self, descricao): #3 4
        self.descricao = descricao # 5
        self.feito = False
        self.criacao = datetime.now()

    def done(self):
        self.feito = True

    def __str__(self): #6
        return f'{self.descricao}' + (' (feito)' if self.feito else '')

def main():
    casa = []
    casa.append(Task('Passar roupa')) #7
    casa.append(Task('Lavar prato'))
    [task.done() for task in casa if task.descricao == 'Lavar prato'] #8
    for task in casa:
        print(f'- {task}')

if __name__ == '__main__':
    main()