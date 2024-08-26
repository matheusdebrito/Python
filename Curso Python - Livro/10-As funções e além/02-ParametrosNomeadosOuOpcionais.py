'''
Os parâmetros opcionais são extremamente úteis para permitir uma maior flexibilidade na função,
assumindo comportamentos padrões (convenção sobre configuração) e diminuindo a API
obrigatória da mesma.
Isso é feito através da definição de valores padrões (default) nos parâmetros, porém há certas
regras:
    • Os parâmetros são processados da esquerda para direita, como existem os parâmetros especiais
que “pegam” vários argumentos, o ordem dos parâmetros (mesmo opcionais) é extremamente
relevante, afetando o resultado final, o ideal é que todos os parâmetros opcionais venham após
os parâmetros posicionais;
    • Valores default podem ser expressões (mas são avaliadas no mesmo momento da definição da
função no namespace);
    • ☠️ Requer muito cuidado ao usar tipos mutáveis.

❶ Definição da classe CSS a ser utilizada quando não for especificada alguma mais específica
❷ Uso da instrução assert para testes simples, caso o teste falhe é levantado uma exceção:
AssertionError
'''

def build_block(texto, classe="sucess"): #1
    return f'<div class="{classe}">{texto}</div>'

#2
assert build_block('Incluído com sucesso') == '<div class="classe">Incluído com sucesso</div>'
assert build_block('Impossível excluir!', 'error') == '<div class="error">Impossível excluir!</div>'

print(build_block('ok'))