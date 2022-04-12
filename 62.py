c=0
x=int(input('Primeiro Termo:'))
y=int(input('Razão:'))
d=int(input('Quantos termos?'))
f=d
while c<d:
    x+=y
    c=c+1
    print(f'a{c}={x}')
e=input('Gostaria de continuar?')
while e=='S':
    a = int(input('Até quanto?'))
    while f<a:
        x+=y
        f=f+1
        print(f'a{f}={x}')
    e=input('Gostaria de continuar?')
print('Finish')

# a=int(input('mais quantos?'))