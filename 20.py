nome = str(input('Digite o seu nome: '))
sexo = str(input('Digite o sexo(f/m): '))
valor = float(input('Digite o valor da compra: '))


if(sexo == 'f'):
    total = (valor * 0.87)
else:
    total = (valor * 0.95)

print('O preço com desconto ficou: ', total)
