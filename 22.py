valor_01 = float(input('Digite o primeiro valor:'))
valor_02 = float(input('Digite o segundo valor:'))

if (valor_01 > valor_02):
    print('O primeiro valor é maior')
elif (valor_01 < valor_02):
    print('O segundo valor é maior')
elif (valor_01 == valor_02):
    print('Não existe valor maior, os dois são iguais')