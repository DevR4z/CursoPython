"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #Espaços a esquerda
print(f'{variavel: <10}') #Espaços a direita
print(f'{variavel: ^10}') #Espaços dos 2 lados
print(f'{variavel:$^10}') #$ dos 2 lados
print(f'{1000.95897643:+,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')