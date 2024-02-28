"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

num1 = input("Digite um numero inteiro: ")
try:
    num_int = int(num1)
    if num_int % 2 == 0:
        print(f'{num_int} é par')
    else:
        print(f'{num_int} é ímpar')
except:
    print("Não foi digitado um número inteiro")

hora = float(input("Digite o horário: "))
if hora >= 0.00 and hora <= 11.59:
    print("Bom dia!")
elif hora >= 12.00 and hora <= 17.59:
    print("Boa tarde!")
elif hora >= 18.00 and hora <= 23.59:
    print("Boa noite!")

nome = input("Digite seu nome: ")
if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) > 4 and len(nome) < 7:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")