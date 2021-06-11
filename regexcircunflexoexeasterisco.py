import re
começaComHelloRegex = re.compile(r'^Hello') # ^ = procura pela palavra Hello no começo da expressão
print(começaComHelloRegex.search('Hello There!'))
print(começaComHelloRegex.search('He said "Hello There!"'))

print('-----------')

terminaComHelloRegex = re.compile(r'world!$')# $ = procura pela palavra world! no final da expressão
print(terminaComHelloRegex.search('Hello world!'))
print(terminaComHelloRegex.search('Hello world!asdfase'))

print('-----------')

allDigitsRegex = re.compile(r'^\d+$') # começa e termina com numeros entre 0 a 9 e pode ter 1 ou mais digitos
print(allDigitsRegex.search('231412352463457456'))  # retorna todos os numero
print(allDigitsRegex.search('231412352x463457456')) # retorna como none pq tem uma letra no meio dos numeros

print('-----------')