peso = 0
altura = 0
somaAltura = 0
mediaAltura = 0
acimaDoPeso = 0
hobits = 0
ogros = 0

for x in range(0, 3):
    peso = float(input('Digite o seu peso: '))
    altura = float(input('Digite a sua altura: '))

    somaAltura += altura

    if(peso >= 90):
        acimaDoPeso += 1
    
    if(peso <= 50 and altura <= 1.60):
        hobits += 1
    
    if(altura >= 1.90 and peso >= 100):
        ogros += 1

mediaAltura = somaAltura / 3
print('Média de altura do grupo:', mediaAltura)
print('Quantidade de pessoas que pesam mais de 90Kg:', acimaDoPeso)
print('Quantidade de pessoas que pesam menos de 50Kg e tem menos de 1.60:', hobits)
print('Quantidade de pessoas que medem mais de 1.90 e pesam mais de 100Kg:', ogros)

