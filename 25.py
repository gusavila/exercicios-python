nomeFuncionario = str(input('Digite o nome do funcionario: '))
salarioFuncionario = float(input('Digite o salário do funcionario: '))
anosTrabalhados = int(input('Digite a quantidade de anos trabalhados na empresa: '))

if(anosTrabalhados <= 3):
    novoSalario = salarioFuncionario * 1.03
elif(anosTrabalhados > 3 and anosTrabalhados < 10):
    novoSalario = salarioFuncionario * 1.125
elif(anosTrabalhados >= 10):
    novoSalario = salarioFuncionario * 1.20

print('Seu novo salário é:',novoSalario)