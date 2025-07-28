# Faça um programa que leia um valor inteiro positivo n e determina a soma dos n primeiros números pares positivos (utilize o comando for).  Ex.: Para 𝑛 = 3, 𝑠𝑜𝑚𝑎 = 2 + 4 + 6. 

entrada = int( input("Digite um número: "))
soma = 0
par = 2

for n in range(0, entrada):
    soma = soma + par
    par += 2
print(f'A soma é {soma}')