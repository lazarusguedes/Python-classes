H = float(input('Altura:'))
W = float(input('Peso:'))
IMC = W/(H**2)
if IMC<18.5:
    print('Abaixo do peso')
elif IMC<=25:
    print('Peso Ideal')
elif IMC<=30:
    print('Sobrepeso')
elif IMC<=40:
    print('Obesidade')
else:
    print('Obesidade mórbida')