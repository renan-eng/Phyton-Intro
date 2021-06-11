import re

prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)
print()
dotStarRegex = re.compile(r'.*')
print('.* - Procura qualquer coisa até achar uma nova linha "\\n"')
print(dotStarRegex.search(prime).group())
print()
dotALLStarRegex = re.compile(r'.*', re.DOTALL)
print('.*, re.DOTALL - Procura qualquer coisa ATÉ CHEGAR AO FINAL DA STR')
print(dotALLStarRegex.search(prime).group())

print('---------------')
# re.I = re.IGNORECASE = n diferenciará entre letras maiusculas e minusculas

vogalRegex = re.compile(r'[aeiou]', re.I)
frase = 'A título de curiosidade, mencione-se a mais acumulada das formações híbridas.'
print(vogalRegex.findall(frase)) # incluir as vogais maiusculas tbm