'''
Em Python temos basicamente dois tipos de parâmetros:

Parâmetro posicional

A posição do parâmetro da lista determina a ordem dos argumentos, todos os posicionais são
obrigatórios, menos o especial (star arg) que utiliza unpacking para receber todo o excesso de
argumentos posicionais

Parâmetro nomeado

A associação entre o argumento e o parâmetro ocorre através do nome, porém excesso de
argumentos posicionais (em relação aos parâmetros definidos) podem ser atribuídos aos
parâmetros nomeados na ordem em que aparecem (esquerda para direita) ou até encontrar o
parâmetro especial posicional (star arg) que é precedido de um asterisco. Os nomeados também
possuem um especial que “pega” qualquer excesso de argumentos nomeados que é precedido de
dois asteriscos. Os parâmetros nomeados devem ter um valor default.

 Os parâmetros especiais normalmente são chamados de *args e **kwargs, sendo
dos tipos tuple e dict respectivamente.

Parâmetro × Argumento
Quando usamos parâmetro nos referimos à variável que receberá o valor passado
pela chamada da função, enquanto argumento é exatamente o valor passado.


'''