X=int(input("I:"))
Y=int(input('II:'))
z=int(input('O que gostaria de fazer:'))
while 0<z<5:
    if z==1:
        print('Soma:',X+Y)
        z = int(input('Diga mais:'))
    elif z==2:
        print(f'Produto:',X*Y)
        z = int(input('Diga mais:'))
    elif z==3:
        if X>Y:
            print(f'Maior número:{X}')
            z = int(input('Diga mais:'))
        elif X<Y:
            print(f'Maior número: {Y}')
            z = int(input('Diga mais:'))
        else:
            print('São iguais')
            z = int(input('Diga mais:'))
    elif z==4:
        X = int(input("I:"))
        Y = int(input('II:'))
        z = int(input('Diga mais:'))
print('Fim')
