menu = """

================ MENU ================

 Digite o numero da operação desejada:
  1 - DEPOSITAR
  2 - SACAR
  3 - EXTRATO
  4 - SAIR
  
=======================================

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Operação realizada com sucesso! {extrato}")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > (saldo - valor)

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if (excedeu_saldo or excedeu_limite or excedeu_saques) and valor > 0:
            print("Operação falhou:")

            if excedeu_saldo:
                print("Você não tem saldo suficiente.")

            if excedeu_limite:
                print("O valor do saque excede o limite.")

            if excedeu_saques:
                print("Quantidade de saques do dia excedido (máximo de 3 saques).")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")