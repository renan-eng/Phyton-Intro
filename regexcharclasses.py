import re

# Caracter Classes:
# \d Any numeric digit from 0 to 9.
# \D Any character that is not a numeric digit from 0 to 9.
# \w Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
# \W Any character that is not a letter, numeric digit, or the underscore character.
# \s Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S Any character that is not a space, tab, or newline.

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a-leaping, 9 ladies dancing, 8 maids a-milking, 7 swans a-swimming, 6 geese a-laying, 5 golden rings, 4 calling birds, 3 French hens, 2 turtle doves'

xmaxRegex = re.compile(r'\d+\s\w+') # aqui o padrão é \d+ (digitos com 1 ou mais numeros) \s (um espaco ' ') \w (qualquer letra)
mo = xmaxRegex.findall(lyrics)
print(mo)

print('-------------------------')