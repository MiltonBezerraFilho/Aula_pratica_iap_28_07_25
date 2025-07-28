#Elabore um programa que mostre todos os números de 1 a 100 e a soma deles.

soma = 0

for n in range(1,101,1):
    soma += n
    print(n)
print(f'A soma é {soma}.')