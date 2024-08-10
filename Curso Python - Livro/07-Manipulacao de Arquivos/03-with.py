"""
❶ A instrução with...as cria um bloco especial de contexto, associado a um determinado
objeto. Ao entrar no bloco o método __enter__() do objeto é executado, e ao encerrar (ou
mesmo em caso de erro) o método __exit__(), simulando um try...finally. Isso torna
essa instrução excelente para manipulação limitada de um objetos em determinados
contextos
❷ A propriedade closed indica se o arquivo está fechado
"""

with open('teste2.txt') as arquivo:#1
    for registro in arquivo:
        print(registro)

if arquivo.closed:#2
    print("Arquivo Fechado")