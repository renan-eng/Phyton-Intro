# Collatz Sequence
def collatz(num):
    if num % 2 == 0:
        num = num / 2
        print(int(num))
        return num
    else:
        num = 3 * num + 1
        print(int(num))
        return num


while True:
    try:
        numero = int(input('Digite um número inteiro positivo: '))
        break
    except ValueError:
        print ('Numero digitado não é inteiro e positivo. Tente novamente.')


while numero != 1:
        numero = collatz(numero)
