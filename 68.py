import randint
c=0
x = input('Par ou Ímpar?')
y = int(input('Número:'))
a = random.randint(0,2)
while True:
    if x=='P':
        print(f'PC:{a}')
        if (y+a)%2==0:
            print('Winneeeer')
            c+=1
            x = input('Par ou Ímpar?')
            y = int(input('Número:'))
            a = random.randint(0, 2)
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
            x = input('Par ou Ímpar?')
            y = int(input('Número:'))
            a = random.randint(0, 2)
print(f'Vitórias Consecutivas:{c}')

