"""Validar e gerador de CPF

INICIAL CPF=168.995.350-09

Algorítimo de validação

1*10=10     ...          """
# CPF INICIAL = '16899535009
from random import randint
numero= str(randint(100000000, 999999999))
novo_cpf = numero
reverso = 10  # contador reverso
total = 0

# Loop do CPF
for index in range(19):
    if index > 8:
        index -= 9    # 9 Primeiros  números

    total += int(novo_cpf[index]) * reverso

    reverso -= 1       # Decremetar o contador
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d =0
        total = 0
        novo_cpf += str(d)

print(novo_cpf)