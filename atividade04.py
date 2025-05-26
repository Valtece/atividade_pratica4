# 4- Crie um programa que solicite números inteiros ao usuário.

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("Número par.")
            pares += 1
        else:
            print("Número ímpar.")
            impares += 1
    except:
        print("Entrada inválida! Digite um número inteiro.")

print(f"\nTotal de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
