# esse programa conta o numero characteres utilizando em um texto

import lorem
import pprint # pretty printer é um modulo que permite exibir dados de uma forma mais bonita e elegante

m = lorem.text()
print(m)
print('------------------------------------------------------------------------------------------------')
count = {}

for x in m.upper(): # o método .upper é utilizado para nao ter diferença entre letras maiusculas e minusculas
    count.setdefault(x, 0) # setdefaul cria uma nova key caso ela ja nao exista.
    count[x] = count[x] + 1 # cada letra dentro do texto sera acidionada ao valor de sua correspondente key

# pprint.pprint(count) # mostra no terminal após a formatação do modulo pprint

contagem = pprint.pformat(count) # o metodo pformat transforma tudo em uma string
print(contagem)