# Como criar sua propia classes de char
import re

vogalRegex = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u|A|E|I|O|U) classe de characteres que representa todas as vogais

letrasMinusculasRegex =  re.compile(r'[a-z]') # considera todas as letras minusculas de a até z

print(vogalRegex.findall('Robocop eats baby food'))

vogalDuplaRegex = re.compile(r'[aeiouAEIOU]{2}') # padrão onde ocorre as vogais 2 vezes repetidas
print(vogalDuplaRegex.findall('Robocop eats baby food'))

print('-------------------------')

# ^ na frente de uma classe é a igual ao not, faz o inverso do que foi especificado

consoantesRegex = re.compile(r'[^aeiouAEIOU]')
print(consoantesRegex.findall('Robocop eats baby food.'))