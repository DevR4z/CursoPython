nome = input('Qual o seu nome: ')
idade = input('Qual a sua idade: ')
espaço = ' '
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if espaço in nome:
        print(f'{nome} contém espaços')
    else:
        print(f'{nome} não contem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')