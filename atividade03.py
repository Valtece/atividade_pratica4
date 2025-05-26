# 3- Crie um programa que verifique se a senha é forte.

while True:
    senha = input("Digite uma senha forte (ou 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break

    if len(senha) >= 8 and any(caractere.isdigit() for caractere in senha):
        print("Senha forte cadastrada com sucesso!")
        break
    else:
        print("Senha fraca! Use pelo menos 8 caracteres e um número.")
