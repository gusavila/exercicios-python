valorCasa = float(input('Digite o valor da casa: '))
salarioComprador = float(input('Digite o salário do comprador: '))
QtdAnosPagar = int(input('Digite a quantidade de anos para pagar: '))

PrestacaoMensal = valorCasa / (QtdAnosPagar * 12)

if (PrestacaoMensal > (salarioComprador * 0.30)):
    print('Empréstimo negado!')
else:
    print('Empréstimo liberado!')