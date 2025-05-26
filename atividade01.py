# 1- Desenvolva uma calculadora que realize as quatro operações básicas (+, -, *, /) entre dois números.

while True:
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        op = input("Digite a operação (+, -, *, /): ")

        if op == "+":
            print("Resultado:", n1 + n2)
            break
        elif op == "-":
            print("Resultado:", n1 - n2)
            break
        elif op == "*":
            print("Resultado:", n1 * n2)
            break
        elif op == "/":
            if n2 == 0:
                print("Erro: divisão por zero.")
            else:
                print("Resultado:", n1 / n2)
                break
        else:
            print("Operação inválida.")
    except:
        print("Erro: entrada inválida.")