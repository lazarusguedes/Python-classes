N = int(input('Escolha um número:'))
I = int(input('Qual será a base de conversão?'))
if I == 1:
    print(f'{N} em binário: {bin(N)[2:]}')
elif I == 2:
    print(f'{N} em octal: {oct(N)[2:]}')
elif I == 3:
    print(f'{N} em hexadecimal: {hex(N)[2:]}')
else:
    print('Errado, animal')