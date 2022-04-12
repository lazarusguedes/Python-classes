Time = int(input('How old is your car?'))

if(Time<=3):
    print('Tá novo!')
else:
    print('Vish, veinho já.')

#ou

print('Tá novo!' if Time<=3 else 'Vish, veinho já.')
print('Done')

n1 = float(input('Primeita Nota:'))
n2 = float(input('Segunda Nota:'))
M = (n1+n2)/2
print(f'Média:{M}')
if M>=7:
    print('Você está aprovado! Boas férias.')
else:
    print('Então né... nos vemos na final.')