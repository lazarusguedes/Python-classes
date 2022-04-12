from random import choice
sample = [0,1,2,3,4,5]
x = choice(sample)
C = int(input('Escolha um número de 0 a 5:'))
if C==x:
    print('Acertou miserávi')
else:
    print('Erooooou')
print(f'O número era {x}')