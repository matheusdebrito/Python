def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo  + alto) // 2
        chute = lista[meio]
        print(baixo)
        print(f"chute: {chute} + item: {item} = {chute + item}")

        if chute == item:
            return f"Elemento encontrado no índice {meio}"
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]
lista_nomes = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]

#print(pesquisa_binaria(minha_lista, 3))

nome = 'banana'

resultado = pesquisa_binaria(lista_nomes, nome)

print(resultado)

