largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))

area = largura * comprimento

if (area < 100):
    print('TERRENO POPULAR')
elif (area <= 500 and area >= 100):
    print('TERRENO MASTER')
elif (area > 500):
    print('TERRENO VIP')