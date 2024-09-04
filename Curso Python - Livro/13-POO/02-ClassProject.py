'''
❶ Como dito anteriormente, é possível declarar uma classe sem informar seu ancestral, e
neste caso é assumido object
❷ Na classe Project teremos uma lista de tarefas que pertencem ao projeto
❸ É possível acessar o atributo tasks e iterar sobre eles
'''
from teste import Task


class Project: #1
    def __init__(self, nome):
        self.nome = nome
        self.tasks = [] #2

    def add(self, descricao):
        self.tasks.append(Task(descricao))

    def pendentes(self):
        return [task for task in self.tasks if not task.feito]
    
    def find(self, descricao):
        return [task for task in self.tasks if task.descricao == descricao][0]
    
    def showTasks(self):
        for task in self.tasks:
            print(f'- {task}')
    
    def __str__(self):
        return f'{self.nome} {len(self.pendentes())} Tarefas pendentes:'
    
def main():
    casa = Project('Casa')
    casa.add('Passar roupa')
    casa.add('Lavar prato')

    mercado = Project('Compras no mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Tomate')

    casa.find('Lavar prato').done()
    print(casa)
    for task in casa.tasks: #3
        print(f'- {task}')
    print('----------------')
    casa.showTasks() # faz a mesma coisa que o for, mas usando um método na própria classe.


    print(mercado)
    for task in mercado.tasks:#3
        print(f'- {task}')
    print('----------------')
    mercado.showTasks() # faz a mesma coisa que o for, mas usando um método na própria classe.

main()