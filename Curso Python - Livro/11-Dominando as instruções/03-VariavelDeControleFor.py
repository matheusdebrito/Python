''''
❶ Variável de controle que indica se encontrou alguma palavra proibida, começa com False
❷ Caso alguma das palavras seja encontrada, ativa a variável de controle, indica que palavra
achou e encerra a iteração
❸ Caso nenhuma palavra seja encontrada (infelizmente só é possível aferir isso após
concluir a iteração), autoriza o texto
'''
PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'politica')

textos = ['joão gosta de futebol e politica', 'A praia foi divertida']

for texto in textos:
    found = False #2
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS: #2
            print(f'A palavra "{palavra}" contida em "{texto}" é proibida. Texto não autorizado.')
            found = True
            break
    
    if not found: #3
        print('Texto autorizado:', texto)