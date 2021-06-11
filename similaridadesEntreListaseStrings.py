import traceback
# Neste programa prodemos ver como uma string pode ser trada com uma Lista

name = 'Renan'
print('O meu nome "Renan" foi guardado em um variável.')
print('Posso utilizar indices e slices da nessa variável da mesma forma que em uma Lista.')
print('Exemplo indice: name[0] = ' + name[0]) # a string Renan possui o indice [0] = R
print('Por exemplo slice: name[1:3] = ' + name[1:3]) # lembrando que no slice o último numero não faz parte da seleção
print('Posso pesquisar com "in" se as letras "en" existem em meu nome => "en" in name = ' + str('en' in name))

# exemplo de for utilizado em uma string

for letras in name:
    print(letras)

print( 'Apesar de listas e strings serem parecidas, a principal diferença é ')
print('Que listas são mutáveis enquanto que uma string é imutável')
print('Por exemplo é possivel acessar uma letra dentro de uma string utilizando o seu indice  => name[1] = ' + name[1])
print('Porém não é possivel alterar uma letra ou outro valor em uma string através do mesmo comando name[1] = 2')
try: 
    name[1] = 'X'
except Exception as erro:
    traceback.print_exc()

# para mudar um caracter ou uma parte de um texto dentro de variável que contem uma str:

nome = 'Zophie a cat'
newName = nome[0:7] + 'the' + nome[8:12]
print(newName)