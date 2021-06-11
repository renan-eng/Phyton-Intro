# metodo .findall()
# findall não retorna um metch object como no search. findall retorna uma lista de str ou de tuplas com grupos de strings
import re

phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

contatoRenan = 'Meu numeros de telefone são: 565-567-66666 e 546-454-7888'

mo = phoneRegex.findall(contatoRenan)
print(mo) # retorna uma lista de todos num conforme o padrão definido em phoneRegex

print('-------------------------')

phoneRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')

contatoRenan = 'Meu numeros de telefone são: 565-567-66666 e 546-454-7888'

mo = phoneRegex.findall(contatoRenan)
print(mo) # retorna uma lista de tuplas com todos os grupos conforme o padrão definido em phoneRegex
print()
phoneRegex = re.compile(r'((\d{3})-(\d{3}-\d{4}))')

contatoRenan = 'Meu numeros de telefone são: 565-567-66666 e 546-454-7888'

mo = phoneRegex.findall(contatoRenan)
print(mo)



