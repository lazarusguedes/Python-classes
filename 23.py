#número --> split --> U,D,C,M --> print
Number = int(input("Number:"))
U = Number % 10
D = Number // 10 % 10
C = Number // 100 % 10
M = Number // 1000 % 10
print(f'Milhar: {M}')
print(f'Centena: {C}')
print(f'Dezena:{D}')
print(f'Unidade:{U}')

#x % 10 --> divide o numero por 10, e dá o resto da divisão (1923 % 10 = 192,3. Resultado: 3)