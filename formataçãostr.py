# string formatting or interpolation

nome = 'Alice'
local = 'Rua Amazonas'
horario = '6 pm'
comida = 'coxinha'

convite = 'Olá ' + nome + ', você está convidada para nossa festa na ' + local + ' às ' + horario + '. Favor trazer ' + comida + '.'
print(convite)
print('--------------')

# com conversion especifiers

convite = 'Olá %s, você está convidada para nossa festa na %s às %s. Favor trazer %s.' % (nome, local, horario, comida)
print(convite)
print('--------------')

# na versão do python 3.6 ou acima é possível utilizar f-strings:

convite = f'Olá {nome}, você está convidada para nossa festa na {local} às {horario}. Favor trazer {comida}.'
print(convite)