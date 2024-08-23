'''
Funções recursivas (que chamam a si mesmas) são bastante comuns nas mais diversas linguagens
de programação, pois normalmente utilizam a sintaxe normal de chamada de funções. Existem
usos bastante interessantes como veremos a seguir.

Toda função recursiva deve ter uma (ou mais) condição(ões) de parada, sem a(s)
qual(is) se tornaria basicamente um loop infinito e pararia em um erro de estouro
de pilha de chamadas (stack overflow), ao consumir todo o espaço dedicado para
tal fim.
Em Python a exceção gerada é RecursionError com a mensagem maximum
recursion depth exceeded.

❶ Chamada recursive a função fatorial()
❷ Condição de parada através do operador ternário
❸ 6 semanas * 7 dias * 24 horas * 60 minutos * 60 segundos = 3628800 segundos
'''

def fatorial(n):
    return n * (fatorial(n - 1) if (n - 1) > 1 else 1) #❶ ❷

if __name__ == '__main__':
    print(f'10! = {fatorial(10)} (6 semanas em segundos)') #❸