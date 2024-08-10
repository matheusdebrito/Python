"""
❶ Uma vez que o arquivo é aberto, o mesmo precisa ser fechado para liberar recursos do
sistema operacional. O try...finally executa o bloco try e depois o bloco finally, mesmo
que haja erro no primeiro bloco, ou seja o bloco finally é de execução obrigatória
❷ Fecha o arquivo, liberando os seus recursos
"""

arquivo = open('testeCSV.csv')
try: #1
    for registro in arquivo:
        print(registro)
finally: #2
    arquivo.close()

if arquivo.closed:
    print("Arquivo fechado")