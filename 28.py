tipoCarro = int(input('Digite (1) para carro Popular ou digite (2) para carros de Luxo: '))
qtdDiasAlugados = int(input('Digite a quantidade de dias alugados: '))
kmPercorridos = float(input('Digite quantos Km foram percorridos: '))

if (tipoCarro == 1):
    precoPagar = 90 * qtdDiasAlugados
    if(kmPercorridos <= 100):
        precoPagar = precoPagar + (kmPercorridos * 0.20)
    elif (kmPercorridos > 100):
        precoPagar = precoPagar + (kmPercorridos * 0.10)

if (tipoCarro == 2):
    precoPagar = 150 * qtdDiasAlugados
    if(kmPercorridos <= 200):
        precoPagar = precoPagar + (kmPercorridos * 0.30)
    elif (kmPercorridos > 200):
        precoPagar = precoPagar + (kmPercorridos * 0.25)

print('Total a pagar: ', precoPagar)