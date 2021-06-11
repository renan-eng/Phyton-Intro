gato = ['gordo', 'laranja', 'agitado']
tamanho, cor, personalidade = gato # atribui cada item de um lista em um variavel distinta
print(tamanho)
print(cor)
print(personalidade)

tamanho, cor, personalidade = 'magro', 'preto', 'qieto'

# Inversao de valores entre variáveis
a = 'AAA'
b = 'BBB'
a, b = b, a # a recebe o valor de b e vice versa
print(a + ' ' + b)


spam = 42
spam += 1 # é o mesmo que spam = spam + 1
spam -= 1 # spam = spam - 1
spam *= 1 # spam = spam * 1
spam /= 1 # spam = spam / 1
spam %- 1 # spam = spam % 1