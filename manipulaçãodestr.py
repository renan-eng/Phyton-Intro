# Esse programa ira apresentar mais formas de manipular str

# aspas duplas "" podem ser usadas da mesma forma que as aspas simples
# vantagem que pode ser usadas aspas simples dentro das asplas duplas

spam = "Thats Alice's cat"

# metodo .upper -> retorna uma versão maiuscula da str

spam = "Hello World!"
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

# .islower retorna um valor booleano True ou falso se a str é toda minúscula

éMin = spam.islower()
print(éMin)
spam = 'Hello world!' # H é maiusculo entao o retor deverá ser Falso
éMin = spam.islower()
print(éMin)

spam = "HELO WORLD!"
éMaiusculo = spam.isupper()
print(éMaiusculo)

# dois métodos podem ser utilizados ao mesmo tempo

teste1 = "Hello".upper().isupper()
print(teste1)
(print('------------------------------------------------------'))

# .isalpha() é Verdadeiro se a str só contem caracters do alfabeto ('letras')

vOuF = 'Hello'.isalpha()
print(vOuF)
vOuF = 'Hello!'.isalpha()
print(vOuF)
vOuF = 'Hello123'.isalpha()
print(vOuF)
print('----------------')

# .isalnum() -> verdadeiro se a str contem letras e numeros

vOuF = 'Hello123'.isalnum()
print(vOuF)
vOuF = 'Hello123!'.isalpha()
print(vOuF)
print('----------------')

# .isdecimal() -> verdadeiro se a str contem numeros

vOuF = '123'.isdecimal()
print(vOuF)
vOuF = '12.4'.isdecimal()
print(vOuF)
print('----------------')

# .isspace() -> verdadeiro se a str contem numeros

vOuF = '     '.isspace()
print(vOuF)
vOuF = ''.isspace()
print(vOuF)
vOuF = 'Hello World'[5].isspace() # na posição 5 existe um espaço logo retorna True
print(vOuF)
print('----------------')

# .istitle() -> verdadeiro se a str contem Texto Formatado Dessa Forma (letra maiuscula no primeiro char)

vOuF = 'É Um Título'.istitle()
print(vOuF)

criarTitulo = 'hello world!'.title() # formata um texto com todas as primeira letras de uma palavra em maiúsculo
print(criarTitulo)
print('----------------')

# .startswith() & .endswith() -> verdadeiro se começa com a letra ou palavra em análise:

vOuF = 'É Um Título'.startswith('É')
print(vOuF)
vOuF = 'Hello'.startswith('Hel')
print(vOuF)
vOuF = 'É Um Título'.endswith('Título')
print(vOuF)
vOuF = 'É Um Título'.endswith('o')
print(vOuF)
print('----------------')

# .join() -> junta qualquer str conforme demonstrado abaixo:

letras = ','.join(['gato','rato','cachorro'])
print(letras+'\n')
letras = '\n\n'.join(['gato','rato','cachorro']) #\n cria uma nova linha dentro do comando print()
print(letras)
print('----------------')

# .split() -> faz o oposto do join

letras = 'Meu nome é Renan'.split()
print(letras)
letras = 'Meu nome é Ramon'.split('m') # utiliza o caracter 'm' como parâmetro de sepração da frase
print(letras)
print('----------------')


# .ljust() & .rjust() -> adiciona espaços ou qualquer caracter que quiser antes (rjust) ou depois (ljust) de uma str

letras = 'Olá'.rjust(10)
print(letras)
tamanhoDaStr = len(letras)
print(tamanhoDaStr)
print()
letras = 'Olá'.ljust(10)
print(letras)
tamanhoDaStr = len(letras)
print(tamanhoDaStr)
print()
letras = 'Olá'.rjust(10, '*')
print(letras)
tamanhoDaStr = len(letras)
print(tamanhoDaStr)
print()
letras = 'Olá'.ljust(10, '*')
print(letras)
tamanhoDaStr = len(letras)
print(tamanhoDaStr)

# .center( -> parecido com ljust e rjust porem centraliza o texto entre o caracter defenido)
letras = 'Olá'.center(10)
print(letras)
tamanhoDaStr = len(letras)
print(tamanhoDaStr)
print()
letras = 'Olá'.center(20, '-')
print(letras)
tamanhoDaStr = len(letras)
print(tamanhoDaStr)
print('----------------')
# .strip -> remove espaços da str

print('            Hello'.strip())
print('            Hello             '.strip())
print('            Hello             '.lstrip())
print('            Hello             '.rstrip())
print('SpamSpamBaconSpamEggsSpamSpam'.strip('Spam'))
print('SpamSpamBaconSpamEggsSpamSpam'.strip('ampS'))

print('----------------')
# .replace -> trocar qualquer char de uma string por outro

print('Hello There!'.replace('e','XYZ'))