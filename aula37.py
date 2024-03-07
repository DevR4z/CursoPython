contador = 0
while contador < 10:
    contador += 1

#   Não mostra o 6
    if contador == 6:
        continue

    print(contador)

    if contador == 4:
        break

print('Acabou')