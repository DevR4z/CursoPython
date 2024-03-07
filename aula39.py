nome = "Luiz Otávio"

letra = 0
tamanho_nome = len(nome)
completo = ''
while letra < tamanho_nome:
    conjunto = nome[letra]
    completo += f'*{conjunto}'
    letra += 1

completo += "*"
print(completo)