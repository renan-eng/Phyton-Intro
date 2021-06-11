import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo) # match object
print(mo.group()) #metodo group retorna um str
# podemos separar grupos de str confome necessidade usando ()
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('-----------------------')
print(mo.group(1)) # retorna somente os 3 primeiros digitos por causa dos ()
print(mo.group(2))

# se precisar encontrar str com '()' então deve se utilizar '\' antes
# .  ^  $  *  +  ?  {  }  [  ]  \  |  (  ) -> são caracteres especiais
# \.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \) -> deve se usar \ antes para detectar esse caracters
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') #r'\(\d\d\d\)' procura por parenteses dentro da str 
mo = phoneNumRegex.search('My number is (415) 555-4242')
print('-----------------------')
print(mo.group())
print(mo.group(1))
print(mo.group(2))
print('-----------------------')

# o padrão anterior pode ser reduzido utilizando {}
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})') #{} indica quantas veses o padrão que procuramos irá se repetir
mo = phoneNumRegex.search('My number is 415-555-4242')
print(mo.group())
print(mo.groups())
areaCode,mainNumber = mo.groups()
print(f'Area Code = {areaCode} and Main number = {mainNumber}')


print('-----------------------')

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # a barra vertical pode ser usada para encontrar várior groupos
mo = batRegex.search('Batmobile losta a wheel')
print(mo.group())
print(mo.group(1))

print('-----------------------')

# o char ? marca que todos os characteres antes deles são opcionais e deve ser reconhecidos no padrão caso exitem

batRegex = re.compile(r'Bat(wo)?man') # irá procurar por Batwoman ou Batman oque acontecer primeiro
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

print('-----------------------')

# utilizando esse conceito podemos fazer uma busca por telefone que tem o códe de area ou não.

phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo = phoneRegex.search('My number is 415-555-4242')
mo2 = phoneRegex.search('My number is 555-4242')
print(mo.group())
print(mo2.group())

print('-----------------------')

# o charaacter * pode ser usado quando vc quer procurar por um padrão de se repete de Zero vezes ou mais

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventures of Batwowowowowowoman')
print(mo.group())

print('-----------------------')

# o charaacter + -> padrão de se repete de uma vez ou mais (obrigatoriamente pelo menos 1 vez)

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batman') # retornas None pq o sinal + obriga o wo acontecer pelo menos uma vez
print(mo)
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwowowowowowoman')
print(mo.group())

print('-----------------------')

# resumo: ? zero ou 1 | * 0 ou mais | + 1 ou mais
# {n} para encontrar um padrão q ser repete n vezes
# {n,m} para encontrar um padrão que se repete no min n vezes e no max m
# {,m} 0 to m
# {3,} 3 to qualquer quantidade

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('My numberers are 415-555-4242,666-2121,413-222-1234')
print(mo.group())

print('-----------------------')

haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('He said "HaHa"')
print(mo)
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())
mo = haRegex.search('He said "HaHaHaHa"')
print(mo.group())
mo = haRegex.search('He said "HaHaHaHaHa"')
print(mo.group())
mo = haRegex.search('He said "HaHaHaHaHaHa"')
print(mo.group())
mo = haRegex.search('He said "HaHaHaHaHaHaHa"') # {3,5} retorna o padrão que se retepe entre 3 e 5 vezes
print(mo.group())

print('-----------------------')


# greedy or non greedy matches
# no exemplo anterior o python sempre retorna o maior numero de repetções possível 5x Ha (greedy)
# para retornar o menor valor utilizar o ? depois da expressão {n,m}?

digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890') # agora será selecionado a menor repetição de digitos
print(mo.group())