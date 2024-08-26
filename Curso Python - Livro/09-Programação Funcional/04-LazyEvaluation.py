'''
Recurso que atrasa o máximo possível um determinado processamento, fazendo-o somente quando
o mesmo for absolutamente necessário, é o inverso de eager evaluation.
Em Python, desde a versão 2.0, diversas funções da biblioteca padrão começaram a ser convertidas
para lazy, um exemplo clássico foi o xrange(), que conviveu até a versão 3 com o range() original. A
diferença é que o range() original retornava um list, totalmente gerada, consumindo todo
processamento e memória de uma vez, enquanto o xrange() retornava uma espécie de generator,
que gerava os valores sob-demanda, gastando menos CPU e consumindo muito menos memória,
pode parecer irrelevante em um range(10), mas se fosse um range(16777216)?
Na versão 3 elas foram unificadas em uma só que retorna um objeto do tipo range, que é um
generator, se for necessário é possível aplicar um eager evaluation transformando-o em outro
objeto, como uma lista ou tupla: list(range(10)). Isso só foi possível pois toda a linguagem foi
ajustada para tornar o uso de generators o mais transparente possível.
Entre as funções que geram generators, temos:
    • map()
    • filter()
    • reversed()
    • range()

Para utilizarmos lazy evaluation em nosso próprio código temos o recurso de generators, que nada
mais é do que uma função que possui retornos parciais, de uma iteração, e que podem ser iteradas
através da função next do __builtins__ até ser totalmente consumida, quando levantam uma
exceção, ainda é possível consumir através de qualquer construção em Python que trabalhe com
iteráveis (como no for, list comprehension, etc), e neste caso o tratamento da exceção é automático.

❶ A instrução yield retorna um valor e suspende a execução da função atual mantendo seu
estado até que uma próxima iteração solicite um novo valor, quando a sua execução
continuará a partir da próxima linha. Caso encontre um novo yield, o ciclo continua, caso
contrário, chegue ao término da função (equivalente a return None) ou execute uma
instrução return explícita, ocorrerá um StopIteration encerrando o iterator
❷ Observe que o retorno da função é um objeto da classe generator
❸ Laço infinito (teoricamente)
❹ Consumindo o próximo valor do iterator (neste caso um generator), através da função
next()


! Como não há tratamento, esta rotina se encerra com um StopIteration
quando não houverem mais valores para consumir

Consumindo um iterator através da instrução for, o próprio Python se encarrega de parar
o laço quando não mais houverem valores a consumir
'''

def cores_arco_iris():
    yield 'vermelho' #1
    yield 'laranja'
    yield 'amarelo'
    yield 'verde'
    yield 'azul'
    yield 'indigo'
    yield 'violeta'

generator = cores_arco_iris()
print(type(generator)) #2

'''while contador == 0: #3
    print(next(generator)) #4'''

for cor in generator:
    print(cor)

print("Fim")