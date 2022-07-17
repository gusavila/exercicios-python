import random
random.seed()
cont = 0
maior = 0
divisivel = 0
while cont < 20:
    sorteio = random.randint(0, 10)
    print(f'Numeros sortiados: {sorteio}')
    cont += 1
    if sorteio > 5:
        maior += 1
    if (sorteio % 3) == 0:
        divisivel += 1

print("Quantidade de numeros maior que 5: ", maior)
print("Quantidade de numeros divisiveis por 3:", divisivel)
