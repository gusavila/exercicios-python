cont = 0
idadeTotal = 0
maiorIdade = 0
menorIdade = 0
maior = menor = 0
while cont < 10:
    idade = int(input("Digite a sua idade: "))
    idadeTotal += idade
    cont += 1
    if idade > 18:
        maiorIdade += 1
    if idade < 5:
        menorIdade += 1
    if cont == 1:
        maior = menor = idade
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade
media = idadeTotal / 10
print("A media de idade do grupo é : ", media)
print("Pessoas maiores de 18 anos: ", maiorIdade)
print("Pessoas com menos de 5 anos: ", menorIdade)
print("Maior idade lida: ", maior)
