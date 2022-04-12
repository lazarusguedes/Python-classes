b=0
x=0
e=int(input('Número:'))
while e!= 999:
    x+=e
    b=b+1
    e=int(input('Número:'))
print(f'Soma Total:{x}')
print(f'Foram utilizados {b} valores')