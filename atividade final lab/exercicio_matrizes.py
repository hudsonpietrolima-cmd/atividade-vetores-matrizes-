matriz = []
for i in range(4):
    print('===================================================')
    matriz.append([])
    for j in range(3):
        print('digite as vendas de camisetas, canecas e bonés, respectivamente:')
        matriz[i].append(int(input()))
print(matriz)

print('quantidade de camisetas vendidas quinta de manhã:', matriz[0][0])
print('quantidade de canecas vendidas quinta de manhã:', matriz[0][1])
print('quantidade de bonés vendidos quinta de manhã:', matriz[0][2])

print('quantidade de camisetas vendidas quinta de tarde:', matriz[1][0])
print('quantidade de canecas vendidas quinta de tarde:', matriz[1][1])
print('quantidade de bonés vendidos quinta de tarde:', matriz[1][2])

print('quantidade de camisetas vendidas sexta de manhã:', matriz[2][0])
print('quantidade de canecas vendidas sexta de manhã:', matriz[2][1])
print('quantidade de bonés vendidas sexta de manhã:', matriz[2][2])

print('quantidade de camisetas vendidas sexta de tarde:', matriz[3][0])
print('quantidade de canecas vendidas sexta de tarde:', matriz[3][1])
print('quantidade de bonés vendidas sexta de tarde:', matriz[3][2])

soma1 = sum(matriz[0])
print('soma das vendas de quinta de manhã:', soma1)
soma2 = sum(matriz[1])
print('soma das vendas de quinta de tarde:', soma2)
soma3 = sum(matriz[2])
print('soma das vendas de sexta de manhã:', soma3)
soma4 = sum(matriz[3])
print('soma das vendas de sexta de tarde:', soma4)