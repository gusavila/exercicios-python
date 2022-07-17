cont = 0
homens = 0
mulheres = 0
idade = 0
idadeTotal = 0
media = 0
idadeHomens = 0
mediaHomens = 0
mulheresMaisVelhas = 0
for cont in range(0, 5):
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("Digite seu sexo: (f ou m):"))
    idadeTotal += idade
    if sexo == 'm':
        homens += 1
        idadeHomens += idade
    elif sexo == 'f':
        mulheres += 1
        if idade >= 20:
            mulheresMaisVelhas += 1
media = idadeTotal / 5
mediaHomens = idadeHomens / homens
print('Quantidade de homens:', homens)
print('Quantidade de mulheres:', mulheres)
print('A media de idade do grupo:', media)
print('A media de idade dos homens é:', mediaHomens)
print('Mulheres que tem mais de 20 anos:', mulheresMaisVelhas)
