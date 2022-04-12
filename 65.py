x = []
d=0
e=int(input('Número:'))
x.append(e)
d+=e
r=d/len(x)
f=input('Gostaria de continuar?')
while f=='S':
    x.append(e)
    d += e
    e = int(input('Número:'))
    f = input('Gostaria de continuar?')
print(f'Maior:{max(x)}')
print(f'Menor:{min(x)}')
print(f'Média:{r}')
