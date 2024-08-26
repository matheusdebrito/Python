'''
❶ Nova função que monta uma lista em HTML (baseada em <ul> e <li>) com todos os
argumentos recebidos (no parâmetro itens, no caso uma tuple)
❷ O conteúdo do bloco será uma lista com os itens: Sábado e Domingo

'''

def build_block(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


def build_list(*itens): #❶
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(build_block('bloco'))
    print(build_block('linha e classe', 'info', True))
    print(build_block('linha', inline=True))
    print(build_block('falhou', classe='error'))
    print(build_block(build_list('Sábado', 'Domingo'), classe='info')) #❷