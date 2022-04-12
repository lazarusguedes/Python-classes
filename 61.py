c = 0
x = int(input('Primeiro termo:'))
r = int(input('Razão:'))
d = int(input('Termos:'))
while c<d:
    x+=r
    c+=1
    print(f'a{c}={x}')
print('The end')