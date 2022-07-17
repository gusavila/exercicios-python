slrAtual = float(input('Digite o valor do seu salário atual: '))
genero = int(input('Digite o número referente ao genero do funcionário (1) para Mulher (2) para Homem : '))
anosTrabalhados = int(input('Quantos anos o funcionário trabalha na empresa? '))

if (genero == 1):
    if (anosTrabalhados < 15):
        novoSlr = slrAtual * 1.05
    elif (anosTrabalhados >= 15 and anosTrabalhados <= 20):
        novoSlr = slrAtual * 1.12
    elif (anosTrabalhados > 20):
        novoSlr = slrAtual * 1.23

if (genero == 2):
    if (anosTrabalhados < 20):
        novoSlr = slrAtual * 1.03
    elif (anosTrabalhados >= 20 and anosTrabalhados <= 30):
        novoSlr = slrAtual * 1.13
    elif (anosTrabalhados > 30):
        novoSlr = slrAtual * 1.25

print('Novo salário é de :', novoSlr, 'Reais')