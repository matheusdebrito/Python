'''
❶ Nova função datetime.timedelta, que é responsável por calcular diferenças entre datas
❷ O constructor da classe Task agora suporta opcionalmente o vencimento da tarefa
❸ A conversão para string agora inclui diversos decoradores, além de feito, temos vencido e
vence em
❹ O método Project.add também suporta opcionalmente a data de vencimento da tarefa
❺ Esta tarefa vence em 3 dias
❻ Tarefa vencida a uma semana
'''

from datetime import datetime, timedelta #1

class Task:
    def __init__(self, descricao, vencimento=None): #2
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento #2
        

    def __str__(self):
        decorators = [] #3
        if self.feito:
            decorators.apend('Status: Feito')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                decorators.append('Status: Vencido')
            else:
                decorators.append(f'Status: Vence em {(self.vencimento - datetime.now()).days} dias')
        else:
            decorators.append('Status: Sem data de vencimento')

        return f'{self.descricao} - ' + ' '.join(decorators)


class Project:
    def __init__(self, nome):
        self.nome = nome
        self.tasks = []

    def add(self, descricao, vencimento=None): #4
        self.tasks.append(Task(descricao, vencimento)) #4

    def __str__(self):
        return f'{self.nome}'

def main():
    casa = Project('Casa')
    casa.add('Passar Roupa')
    casa.add('Lavar Prato')
    casa.add('Arrumar o guarda-roupa', datetime.now() + timedelta(days=3)) #5
    casa.add('Pintar', datetime.now() - timedelta(days=7)) #6
    print(casa)
    for task in casa.tasks:
        print(task)

main()
        