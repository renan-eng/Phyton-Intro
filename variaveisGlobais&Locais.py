spam = 42 # variavel global

def eggs(): # cada função tem seu espaço para variaveis locais
    spam = 42 # variavel local
    # as variáveis locais são temporárias, elas só existem durante a executação da função
    # logo após o retorno da função todas as variaveis locais dessa função são apagadas
    # variáveis locais não pode ser usadas como variáveis globais

print('Algum código aqui.')
print('Algum código aqui.')


# exemplo de uso incorreto de variáveis local:
# def spam():
#     eggs = 99

# spam()
# print(eggs)

# varial local de uma função nao irá modificar outra variável local de outra função mesmo se tiver o mesmo nome,
# pois as várias só existem dentro do seu escopo local:
def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam() #o valor impresso na função spam será 99, pois o valor 0 atribuido a eggs em outra função só existe local mentro dentro da função bacon()
# este exemplo demonstra que as variáveis dentro de uma função são totalmente separadas de outra função, elas são instâncias independentes.

# podemos usar variáveis globais dentro de funções:
# quando uma variáveis é chamada dentro de uma função porém ela não foi definida dentro da função
# python irá procurar por uma variável que foi definida no escopo global de varáveis
def spam():
    eggs = 'Olá'
    print(eggs) # irá mostrar na tela o valor Olá

eggs = 42
spam()
print(eggs) # irá mostrar o valor 42

# no exemplo abaixo podemos obrigar o programa a considerar uma variável dentro de uma funçao como global
def spam():
    global eggs # define eggs como global
    eggs = 'Olá'
    print(eggs) # irá mostrar na tela o valor global para eggs Olá

eggs = 42
print(eggs) #altera o valor global de eggs para 42
spam()
print(eggs) # irá mostrar o valor Olá pq foi modificado globamente dentro da função spam