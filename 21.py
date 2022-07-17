distancia = float(input('Qual a distancia(em Km) deseja percorrer?'))

if (distancia <= 200):
    precoPassagem = distancia * 0.50
else:
    precoPassagem = distancia * 0.45

print('Valor da passagem: ', precoPassagem, 'R$')

