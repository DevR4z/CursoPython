valor1 = input('Digite um valor: ')
valor2 = input('Digite outro valor: ')

if valor1 > valor2:
    print(f'{valor1=} é maior do que {valor2=}')
elif valor2 > valor1:
    print(f'{valor2=} é maior do que {valor1=}')
else:
    print(f'Os valores são iguais')