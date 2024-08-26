'''
❶ Novo parâmetro nomeado: inline, que indicará se será usado o <span> ou <div>
❷ Definição da tag principal conforme parâmetro inline
❸ É possível passar uma argumento posicional para o inline, sendo o terceiro
❹ Podemos nomear nossos argumentos para definir (independente da ordem) determinados
parâmetros na função
'''

def build_block(texto, classe='sucess', inline=False): #1
    tag = 'span' if inline else 'div' #2
    return f'<{tag} class="{classe}">{texto}</{tag}>'


print(build_block('bloco'))
print(build_block('linha e classe', 'info', True)) #❸
print(build_block('linha', inline=True)) #❹
print(build_block('falhou', classe='error')) #❹