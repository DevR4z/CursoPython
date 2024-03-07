while True:
    num1 = input()
    num2 = input()
    op = input()

    num_validos = None

    try:
        num1_f = float(num1)
        num2_f = float(num2)
        num_validos = True
    except:
        num_validos = None
    
    if num_validos is None:
        print('Um ou ambos números digitados são inválidos.')
        continue

    op_permitidos = '+-/*'
    if op not in op_permitidos:
        print('Operador inválido.')
        continue
    if len(op) > 1:
        print('Digite apenas um operador.')
        continue

    print('Resultado:')

    if op == '+':
        print(f'{num1_f} + {num2_f} =',num1_f + num2_f)
    elif op == '-':
        print(f'{num1_f} - {num2_f} =',num1_f - num2_f)
    elif op == '/':
        print(f'{num1_f} / {num2_f} =',num1_f / num2_f)
    elif op == '*':
        print(f'{num1_f} * {num2_f} =',num1_f * num2_f)
    else:
        print('Nunca deveria chegar aqui...')
    

    ###
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break
