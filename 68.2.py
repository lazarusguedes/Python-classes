from random import randint
c=0
while True:
    x = input('Par ou Ímpar?')
    y = int(input('Número:'))
    a = randint(0,2)
    if x=='P':
        print(f'PC:{a}')
        if (y+a)%2==0:
            print('Winneeeer')
            c+=1
        else:
            print('Loseeeeer')
            break
    elif x=='I':
        print(f'PC:{a}')
        if (y+a)%2==0:
            print('Loseeeeer')
            break
        else:
            print('Winneeeer')
            c+=1
print(f'Vitórias Consecutivas:{c}')

