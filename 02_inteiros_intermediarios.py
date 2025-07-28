#Faça um programa que leia dois números inteiros e depois mostre todos os inteiros entre eles.

numero_1 = int( input("Digite o primeiro número: "))
numero_2 = int( input("Digite o segundo número: "))

for n in range(numero_1 + 1, numero_2):
    print(n)