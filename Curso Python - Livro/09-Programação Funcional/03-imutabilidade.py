'''
Imutabilidade ou a arte de não causar efeitos colaterais. Representados aqui por tipos como tuple,
set, frozenset, int, str e muito mais além dos recursos de fatiamento e funções de transformação
de iteráveis (como listas e tuplas), gerando um novo objeto (sem alterar o original), como: map(),
filter(), sorted(), reversed(), etc.
Um objeto (ou variável de tipo primitivo) imutável tem algumas características interessantes, como:
    • Redução (ou eliminação) de efeitos colaterais;
    • Alta testabilidade;
    • Funções puras, que permitem o uso cache facilmente;
    • Entre outras.

O módulo locale da biblioteca padrão, possui diversas funcionalidades relativas a
internacionalização (i18n) e localização. Neste caso estamos usando o setlocale e a
constante LC_ALL
❷ O módulo calendar possui diversas funções auxiliares para impressão de calendário,
incluindo aí traduções e helpers como os nomes do meses (month_name), e a quantidade de
dias de cada mês (mdays), conforme o locale.
❸ A função functools.reduce (que no Python 2 ficava no __builtins__), permite a iteração de
um iterable qualquer de forma acumulativa, pegando o resultado da última iteração e
passando como parâmetro para a próxima, em conjunto com o elemento atual sendo
iterado.
❹ Configura o locale atual no processo em execução para pt_BR (usando UTF-8 como
encoding)
❺ A função reduce() recebe três argumentos:
1. Função que será usada para o processamento (redução em um único valor);
2. Objeto que será iterado (iterable);
3. Valor inicial, que será usado como o acumulado anterior para o primeiro item.
❻ Função anônima usada pelo reduce() que concatena o texto acumulado anterior e
adiciona uma nova linha com o nome do mês
❼ A função map() aqui é usada para mapear um faixa de 1 a 12 no seu nome de mês
equivalente
❽ Função anônima usada pelo map() para converter o número do mês em seu nome
❾ A função filter() está selecionando para a função map() apenas aqueles meses que tem 31
'''

from locale import setlocale, LC_ALL #❶
from calendar import mdays, month_name #❷
from functools import reduce #❸
# Português do Brasil
setlocale(LC_ALL, 'pt_BR.utf8') #❹
# Listar todos os meses do ano com 31 dias
# Funcional bem formatado
print(
    reduce( #❺
        lambda output, nome_mes: f'{output}\n- {nome_mes}', #❻
        map( #❼
            lambda mes: month_name[mes], #❽
            filter( #❾
                lambda mes: mdays[mes] == 31, #❿
                range(1, len(month_name)) #⓫
            )
        ),
        'Meses com 31 dias:', #⓬
    )
)