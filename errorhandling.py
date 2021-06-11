def div42por(divisor):
    try:
        return 42 / divisor
    except ZeroDivisionError: # tipo de erro que o programa deve exibir os comandos abaixo
        print('Erro: Divisão por zero.')

print (div42por(2))
print (div42por(12))
print (div42por(0))
print (div42por(1))

# é possivel usar try and except sem especificar o tipo de erro

print('Quantos gatos você tem?')
numGatos = input()
try:
    if int(numGatos) >= 4:
        print('Você tem muitos gatos.')
    else:
        print('Você não tem muitos gatos.')
except ValueError:
    print('Você não digitou um número.')