saldo = 0.0
LIMITE_SAQUE = 500.0
LIMITE_SAQUES_DIARIOS = 3
extrato_depositos = []
extrato_saques = []
numero_saques = 0

MENU = """
=== Sistema Bancário ===
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=======================
"""

def deposito(saldo, extrato):
    print("\n=== Depósito ===")
    try:
        valor = float(input("Digite o valor para depósito: R$ "))
        if valor <= 0:
            print("ERRO: Valor deve ser positivo!")
        else:
            saldo += valor
            extrato.append(f"+ R$ {valor:.2f}")
            print(f"Depósito realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
    except ValueError:
        print("ERRO: Entrada inválida! Digite apenas números.")
    return saldo

def saque(saldo, extrato, saques_realizados):
    print("\n=== Saque ===")
    if saques_realizados >= LIMITE_SAQUES_DIARIOS:
        print("ERRO: Limite diário de saques atingido.")
        return saldo, saques_realizados

    try:
        valor = float(input("Digite o valor para saque: R$ "))
        if valor <= 0:
            print("ERRO: Valor deve ser positivo!")
        elif valor > LIMITE_SAQUE:
            print(f"ERRO: Limite por saque é de R$ {LIMITE_SAQUE:.2f}")
        elif valor > saldo:
            print(f"ERRO: Saldo insuficiente. Saldo atual: R$ {saldo:.2f}")
        else:
            saldo -= valor
            extrato.append(f"- R$ {valor:.2f}")
            saques_realizados += 1
            print(f"Saque realizado! Novo saldo: R$ {saldo:.2f}")
    except ValueError:
        print("ERRO: Entrada inválida! Digite apenas números.")
    return saldo, saques_realizados

def extrato(saldo1, depositos, saques):
    print("\n=== Extrato ===")
    if not depositos and not saques:
        print("Nenhuma movimentação realizada.")
    else:
        print("Depósitos:")
        for item in depositos:
            print(item)
        print("\nSaques:")
        for item in saques:
            print(item)
    print(f"\nSaldo atual: R$ {saldo:.2f}")

# Loop principal do menu
while True:
    print(MENU)
    opcao = input("Escolha uma opção: ").lower()

    if opcao == "q":
        print("Obrigado por utilizar o sistema bancário. Até logo!")
        break
    elif opcao == "d":
        saldo = deposito(saldo, extrato_depositos)
    elif opcao == "s":
        saldo, numero_saques = saque(saldo, extrato_saques, numero_saques)
    elif opcao == "e":
        extrato(saldo, extrato_depositos, extrato_saques)
    else:
        print("Opção inválida! Tente novamente.")

    print("=======================\n")