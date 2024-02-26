nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade)) #format n ta fazendo anda

nome2 = 'Luiz'
idade2 = 23
formato = '{n} tem {i} anos'
print (formato.format(n=nome2, i=idade2))

div = 4 / 2
print(div) # / sempre vira float