velocidade = float(input('Qual a velocidade(em Km) do carro? '))

if (velocidade > 80):
    multa = (velocidade - 80) * 5
    print('Você foi multado\n'
    'Valor da multa: ', multa, 'R$')