# a função len() retorna o tamanho da lista e pode ser usado em conjunto 
# com a função range() dentro do forloop para retorna o index e o item da lista
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
        print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

print('_____________________________________________________________________________________')

# a função enumerate()  retorna o index e o item da lista em cada iteração do for loop
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supllies is: ' + item)