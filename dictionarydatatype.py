# para criar uma variavel do tipo dicionario vamos utilizar '{}',
# primeiro temos a keyword : valor serpados por ',' como no exemplo abaixo
myCat = {'size':'fat', 'color':'gray', 'disposition':'loud'}
print(myCat['size'])
print(myCat['color'])

# diferente de listas, o tipo de dados Dicionario nao tem ordem
myCat = {'size':'fat', 'color':'gray', 'disposition':'loud'}
myCat2 = {'color':'gray', 'disposition':'loud', 'size':'fat'}
print(myCat == myCat2)

# as keys, items e ambos podem ser tranformados em uma lista utilizando as funções:
# dict.keys(), dict.values(), dict.item()
keys1 = list(myCat.keys())
print(keys1)
values = list(myCat.values())
print(values)
items= list(myCat.items())
print(items)

# essas funções podem ser utilizadas diretamente no foor loop para manipulações de
# qualquer um desses dados.
for k in myCat.keys():
    print(k)

for v in myCat.values():
    print(v)

for k, v in myCat.items():
    print(k, v)

# o metodo get() tem dois arguimentos, o primeiro ira retornar o valor daquela key
# dentro de um dicionario, o segundo argumento é um valor padrão para caso essa key nao exista

print(myCat.get('color', 0))
print(myCat.get('age', 0))

# o metodo setdefault() é o inverso do get(), esse metodo irá incluir uma key e seu valor
# se e somente se essa key já não existe no dicionario

myCat.setdefault('age', 8)
print(myCat) # agora meu dicionario myCat tem a key 'age' com o valor de 8

myCat.setdefault('age', 10) # como essa key ja existe esse comando será ignorado pelo compilador
print(myCat) # age continua como 8


