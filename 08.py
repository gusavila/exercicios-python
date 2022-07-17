metros = float(input('Digite a distância em metros: '))

print(
    'A distância de', metros, 'corresponde a:\n',
    metros / 1000, ' Km     |    ', metros * 10,   'dm\n',
    metros /  100, ' Hm     |    ', metros * 100,  'cm\n',
    metros /   10, 'Dam     |    ', metros * 1000, 'mm'
)