'''
Escreva um programa que leia idades de uma turma de alunos e calcule a maior e a menor 
idades informadas. O número de alunos da turma deve ser informado pelo usuário. Dica: 
Você deve usar variáveis auxiliares (maior e menor) para manter a maior e a menor nota 
digitadas pelo usuário. No caso da maior nota, você deve verificar, a cada iteração, se a 
nota atual digitada pelo usuário é maior que a variável maior. Em caso positivo, você 
dever atribuir tal valor à variável maior. Para a menor nota, o raciocínio é similar.
'''

maior = -1
menor = 101

numero_alunos = int( input("Digite o número de alunos: "))

for n in range(0,numero_alunos):
    nota = float(input("Digite uma nota: "))
    if (nota > maior):
        maior = nota
    if (nota < menor):
        menor = nota
if (maior == -1 and menor == 101):
    print("Valores de nota inválidas")
else:
    print(f"A maior nota foi {maior} e a menor nota foi {menor}")
