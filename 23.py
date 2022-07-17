nota_01 = float(input('Digite o valor da primeira nota: '))
nota_02 = float(input('Digite o valor da segunda nota: '))

media = (nota_01 + nota_02) / 2

if (media < 5):
    print('REPROVADO')
elif (media > 5 and media < 7):
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
