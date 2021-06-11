spam = ['hello', 'hi', 'howdy', 'heyas']
indice = spam.index('hello') # index é um método que retorna o indice de determinado valor em uma lista
print(indice) # o indice de 'hello' é igual a 0

# index retorna o indice onde localizou primeiro o valor procurado

nome = ['Roberto', 'Renata', 'Jose', 'Renata']
nomeIndice = nome.index('Renata') # o indice retorno é aonde há o primeira aparição da variavel buscada
print(nomeIndice)

# append Method

lista = ['gato', 'cachorro', 'rato']
lista2 = lista.append('vaca')
print(str(lista))
print(str(lista2))
lista.remove('rato')
print(str(lista))

# Obs.: os metodos append, insert e remove só funcionam em listas 
# o metodo remove deleta a primeira vez que o termo aparece na lista (termos repetidos)

# sort method => É ordenado de acordo com a tabela "ASCII-betical" pesquisar para mais detales

lista = ['abelha', 'elefante', 'golfinho', 'baleia', 'foca']
lista.sort()
print(str(lista))
numOrd = [2, 5, 3.14, 1, -7]
numOrd2 = [2, 5, 3.14, 1, -7]
numOrd.sort()
numOrd2.sort(reverse=True) # reverse=True altera a ordenação para o inverso da padrão
print(numOrd)
print('--------------------------------------------------------------------------------------')
print(numOrd2)
#Exemplo de ordenação por ASCII:

ord = ['Alice', 'Bob', 'renan', 'Caroline', 'caveira', 'Zeus']
ord.sort()
print(str(ord))

# Todas as letras maiusculas em ASCII vem antes das letras minusculas
# Para alterar esse comportamento e ordenar em alfabeticamente:

lista = ['A', 'Z', 'a', 'z']
lista1 = ['a', 'z', 'A', 'Z']
lista.sort(key=str.lower)
lista1.sort(key=str.lower)
print(lista)
print(lista1)