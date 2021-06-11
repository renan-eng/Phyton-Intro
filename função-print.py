 #o argumento end substitui o comportamento padrão da função print()
 #sem nenhum argumento adicional a funcão print sempre cria uma nova linha após sua chamada
print('Olá', end=' ')
print('Mundo')
print()
#ao colocar variás str seprados por ',' veremos no terminal as palavras separadas por um espaço
print('gato', 'cachorro', 'rato')
print()

#para separar os argumentos dentro de uma função print por qualquer outro caracter utilizar a o argumento sep=
print('gato', 'cachorro', 'rato', sep='ABC')