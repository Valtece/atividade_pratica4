# 2- Crie um programa para o professor registrar as notas da turma.

notas = []

while True:
    entrada = input("Digite a nota (ou 'fim' para encerrar): ").lower()

    if entrada == 'fim':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite um valor entre 0 e 10.")
    except:
        print("Entrada inválida! Digite uma nota numérica ou 'fim'.")

# Cálculo da média
if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")

