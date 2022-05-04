main = []
pesos = []
while True:
    reference = []
    name = input('Nome:')
    peso = int(input('Peso:'))
    reference.append(name)
    reference.append(peso)
    main.append(reference[:])
    pesos.append(peso)
    reference.clear()
    pausa = input('Gostaria de continuar? (S/N) ')
    if pausa == 'N':
        break
base = 0
mais_pesados = []
mais_leve = []
for c in range (len(pesos)):
    if pesos[base] == min(pesos):
        mais_leve.append(main[base][0])
    elif pesos[base] == max(pesos):
        mais_pesados.append(main[base][0])
    base+=1
print(f'Foram cadastradas {len(main)} pessoas ')
print(f'mais_leves: {len(mais_leve)}')
if len(mais_pesados) == 1:
    print(f'O mais pesado foi {mais_pesados}, com {max(pesos)} Kg')
else:
    print(f'Os mais pesados foram {mais_pesados}, com {max(pesos)} Kg')

if len(mais_leve) == 1:
    print(f'O mais leve foi {mais_leve}, com {min(pesos)} Kg')
else:
    print(f'Os mais leves foram {mais_leve}, com {min(pesos)} Kg')