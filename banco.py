print('Olá!!! Bem vindo ao banco! Selecione alguma opção: ')

menu = """
[1] Sacar
[2] Depositar
[3] Extrato
[4] Sair
"""

saldo = 0
limite = 500
extrato = ""
saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        if saques < limite_saques:
            try:
                valor_saque = float(input('Informe o valor que deseja sacar: '))
                if (valor_saque > 0):
                    if valor_saque <= saldo:
                        if valor_saque <= limite:
                            saldo -= valor_saque
                            saques += 1
                            extrato += f"Saque: R$ {valor_saque:.2f}\n"
                            print(f"Saque realizado! Saldo atual: R$ {saldo:.2f}")
                        else:
                            print("Limite de R$ 500 por saque!")
                    else:
                        print('Saldo insuficiente')
                else:
                    print("Valor inválido. Digite um valor válido.")
            except ValueError:
                print("Valor inválido. Digite um número.")
        else:
            print('Limite de saques excedidos')

    elif opcao == "2":
        try:
            valor_deposito = float(input('Informe o valor que deseja depositar: '))
            if valor_deposito > 0:
                saldo += valor_deposito
                extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
                print(f'Depósito de R$ {valor_deposito:.2f} realizado! Saldo atual: R$ {saldo:.2f}')
            else:
                print("Valor inválido. Digite um valor positivo para depositar.")
        except ValueError:
            print("Valor inválido. Digite um número.")

    elif opcao == "3":
        print(f'Seu extrato é de: {extrato}')
    
    elif opcao == "4":
        print("Saindo!Agradecemos a preferência :)")
        break

