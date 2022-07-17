cont = 0
maior = 0
menor = 0

for cont in range(0, 8):
    valorProdutos = float(input("Digite o valor do produto: "))
    cont += 1
    if cont == 1:
        maior = menor = valorProdutos
    else:
        if valorProdutos > maior:
            maior = valorProdutos
        if valorProdutos < menor:
            menor = valorProdutos
print('O maior é :', maior)
print('O menor é :', menor)
