from random import choice
sample = [0,1,2,3,4,5,6,7,8,9,10]
A=1
x = choice(sample)
C = int(input('Escolha um número de 0 a 10:'))
while x!=C:
    print('Eroooooou!!!!')
    C=int(input('Mais uma vez:'))
    A=A+1
if A==1:
    print(f'Acertou miserávi, e só precisou de 1 chance.')
else:
    print(f'Acertou miserávi, e só precisou de {A} chances.')

