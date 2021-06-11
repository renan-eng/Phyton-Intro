# Listas são elementos dentro '[]' separados por uma ','
# variável[i] onde i é o indice que representa a posição de cada elemento.
# toda lista começa com o índice 0 (zero)
spam = ['cat', 'bat', 'rat', 'elephant']
print('Criei uma váriavel chamada "spam" e atribua a lista ["cat", "bat", "rat", "elephant"]' )
print('spam = ' + str(spam))
print('spam[0] = ' + spam[0])
print('spam[1] = ' + spam[1])
print('spam[2] = ' + spam[2])
print('spam[3] = ' + spam[3])
# OBS.: Slices exibe os multiplos valores dentro do índices [x:y] exceto o valor de y
print('spam[1:3] = ' + str(spam[1:3]) + ' *Obs.:Não inclui o índice 3, somente 1 e 2.')
print()

print('Listas dentro de listas: ')

# Listas dentro de listas

exemplo = [['gato', 'morçego'], [10, 20, 30, 40, 50]]
print('Exemplo = ' + str(exemplo)) # exibe a lista completa
print('Exemplo[0] = ' + str(exemplo[0])) # exibe a primeira lista dentro da lista completa => ['gato', 'morçego']
print('Exemplo[0][1] = ' + exemplo[0][1]) # exbie o segundo elemento dentro da primeira lista => morçego
print('Exemplo[1][4] = ' + str(exemplo[1][4])) # exbie o quarto elemento dentro do segundo item da lista completa => 50
print()

print('Índices negativos: ')

# Indices podem ser negativos tbm, porem irão exibir os item na ordem inversa da lista
# -1 exibe o último item, -2 o penultimo item ....

exemplo2 = ['cat', 'bat', 'rat', 'elephant']
print('Exemplo2 = ' + str(exemplo2))
print('Exemplo2[-1] = ' + exemplo2[-1])
print('Exemplo2[-2] = ' + exemplo2[-2])
print('Exemplo2[-3] = ' + exemplo2[-3])
print('Exemplo2[-4] = ' + exemplo2[-4])