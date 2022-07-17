anoNascimento = int(input('Digite o seu ano de nascimento: '))
idade = 2022 - anoNascimento

if(idade < 16):
    print('Você não pode votar!')
else:
    print('Você pode votar!')