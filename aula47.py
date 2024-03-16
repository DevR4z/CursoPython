palavra = 'animal'
tentativa = input('Digite uma letra: ')
i = 0
x = ''
if len(tentativa) > 1:
    print('Digite apenas uma letra.')
    tentativa = input('Digite uma letra: ')
elif tentativa.__str__ == None:
    print('Isso não é uma letra')
while i < len(palavra):
    if tentativa == palavra[i]:
        if i == 0:
            i = 1
        antes = '*' * i
        dps = len(palavra) - i - 1
        depois = '*' * dps
        formato = (antes + tentativa + depois)
    i += 1
    qtd = tentativa in palavra
if qtd == False:
   print('*' * len(palavra))
if qtd == True:
    print(formato)


    

