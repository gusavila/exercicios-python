par = 0
impar = 0
for x in range(0, 6):
    num = int(input('Digite um numero: '))
    if((num % 2) == 0):
        par += 1
    else:
        impar += 1

print('Pares = ', par)
print('Impares = ', impar)
