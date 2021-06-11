# Continuação da introdução sobre listas
# Inserir valores na lista pode ser feito simplesmente:

spam = [10, 20 , 30, 40]
spam[1] = 'Olá' # o item[1] = 20 é trocado pela string Olá
print(str(spam))
spam[1:3] = ['GATO', 'CACHORRO', 'RATO'] # insire os itens GATO, CACHORRO E RATO NOS INDICES 1 E 2 DA LISTA SPAM
print(str(spam))


# Slices podem ser resumidos da seguinte maneira:
print()
print('************')
spam = [10, 20, 30, 40, 50]
print(str(spam[:2])) # Desta maneira o compilador considera que o primeiro item é o 0 por padrão e exibe [0:2]
print(str(spam[1:])) # O oposto tbm funciona, pega o valor indicado e para no final da lista

# Desatribuir um indice especifico da Lista
print()
print('************')
spam = [10, 20, 30, 40, 50]
del spam[2] # deleta o valor contido no indice 2 => apaga o valor 30 e move todos os outros valores um casa para prencher o lugar vazio
print(str(spam))

# Comando len() para listas
print()
print('************')
tamanhoDaLista = len([1, 2, 4, 6]) # o tamanho dessa lista será 4 pois contem 4 valores numericos 
print(tamanhoDaLista)

# Adição de duas listas
print()
print('************')
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
lista3 = lista1 + lista2 # a lista3 será [1, 2, 3, 4, 5, 6, 7, 8]
print(lista3)

# Multiplicação de lista
print()
print('************')
lista = [1, 2, 3]
print(lista * 3) # cria uma nova lista com os valores da lista repetidos 3 vezes

# Função list()
print()
print('************')
lista = list('Olá Mundo') 
print(lista)
numeroParAte98 = list(range(0, 100, 2))
print(numeroParAte98)
print()
print('************')

# in comando

estado = 'colé' in ['oi', 'ola', 'colé', 'aba'] # a variavel estado recebe o valor TRUE pois colé existe dentro do lista analisado por 'in'
print(estado)
estado2 = 'cole' in ['oi', 'ola', 'colé', 'aba'] # a variavel estado recebe o valor FALSE pois colé NÃO existe dentro do lista analisado por 'in'
print(estado2)

estado = 'colé' not in ['oi', 'ola', 'colé', 'aba'] # a variavel estado recebe o valor FALSO pois colé existe dentro do lista analisado por 'in'
print(estado)