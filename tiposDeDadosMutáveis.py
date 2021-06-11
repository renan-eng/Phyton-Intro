# Diferenças entre tipos de dodos mutáveis e não mutáveis

# Utilizando uma string vemos que a função nao altera o valor da variavel global
def eggs(cheese):
    cheese = 'Hello' #local 

spam = '1, 2, 3' #global
eggs(spam)
print(spam)

# utilizando uma lista, a alteração acontece pq a variavel local esta referenciando a mesma lista da variavel global
def eggs(cheese):
    cheese.append('Hello') #local 

spam = [1, 2, 3] #global
eggs(spam)
print(spam)

# para economizar recursos do pc python utiliza esse recurso de referência para nao ter copiar lista duas vezes sem necessidade'Hello''Hello'

# para copiar uma lista para outra variavel deve ser usar o modulo copy
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam) # se a lista nao for copiada com esse comando, qualquer mudança na varia cheese ira afetar a variavel spam
cheese[1] = 42
print(cheese)
print(spam)

# uma lista pode ser escrita em linhas diferentes como no exemplo abaixo sem problemas nenhum
spam = ['apples',
        'oranges',
        'banans',
        'cats']
print(spam)

# se quiser dividir parte do seu cógido em linhas separadas pode utilizar o '\'
print('Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Curabitur iaculis quis diam sed imperdiet. Curabitur fringilla eros rutrum accumsan dictum. ')