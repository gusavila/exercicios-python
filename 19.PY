anoNascimento = int(input('Digite o seu ano de nascimento: '))
idade = 2022 - anoNascimento

if(idade < 18):
    print('Faltam ', 18 - idade, 'para o alistamento!')
else:
    print('Ja se passaram',  idade - 18 , 'desde o alistamento!')