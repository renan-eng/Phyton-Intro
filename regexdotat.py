import re

atRegex = re.compile(r'.at') # procura por qualquer pradrao que contem .(qualquer coisa)+at ao mesmo tempo
# retorna car, hat, sat, lat, mat (obs que nao vem flat e sim lat pois . só terona o primeiro caracter antes do at)
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

print('---------------')

atRegex = re.compile(r'.{1,2}at') # procura por qualquer pradrao que contem .(qualquer coisa)+at ao mesmo tempo
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

print('---------------')

nomeCompleto = 'Primeiro Nome: Renan Último Nome: Guimarães'
#.* procurar por qualquer coisa na expressão:
nameRegex = re.compile(r'Primeiro Nome: (.*) Último Nome: (.*)')
mo = nameRegex.search(nomeCompleto) # lembrar que search retorna um mo (match object)
primeiroNome, últimoNome = mo.group(1), mo.group(2)

nome = nameRegex.findall(nomeCompleto) # lembrar que findall retorna uma lista
primeiroNome1, ultimoNome1 = nome[0]

print(f'{primeiroNome} {últimoNome}')
print(primeiroNome1, ultimoNome1)

print('---------------')

# .* = greedy
# .*? = non-greedy veja a diferença no exemplo abaixo
serve = '<To serve humans> for dinner.>'

print(serve)
print()
#procura por qualquer coisa entre os caracteres < >
greedyRegex = re.compile(r'<(.*)>') 
print(greedyRegex.findall(serve))

nonGreedyRegex = re.compile(r'<(.*?)>')
print() 
print(nonGreedyRegex.findall(serve))

print('---------------')
