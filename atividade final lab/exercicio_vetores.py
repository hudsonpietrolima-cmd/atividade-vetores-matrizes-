vetor = []

for i in range(5):
    V = int(input('digite a quantidade de chamados de segunda a sexta'))
    vetor.append(V)
    print('chamados de segunda a sexta:')
    print(vetor)

soma = sum(vetor)
print('total de chamados durante a semana:', soma)

média = soma / 5
print('média de chamados durante a semana:', média)

maior = vetor.index(max(vetor))
print('maior numero de chamados no dia:', vetor[maior])

