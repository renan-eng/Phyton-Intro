def spam():
    global eggs
    eggs='spam' # global

def bacon():
    eggs = 'local' # local

def ham():
    print(eggs) # use global 

eggs = 42 # global
spam()
print(eggs)

# se em algum momento vc precisar se modificar uma variavel global dentro de uma função
# deverá utilizar o comando global para isso, caso contrário vc irá criar uma variável local
# que não tem nada a ver com a variavel global.
# Exemplo de erro ao chamar uma variavel global dentro de uma funcão que ja existe uma variavel com mesmo nome:
# def spam():
#     print(eggs) # ERROR pois python ja sabe que essa variável existe dentro da sua função porem não foi definada ainda (e não usará o valor global desta variável)
#     eggs = 'spam local'

# eggs = 'global'
# spam() 