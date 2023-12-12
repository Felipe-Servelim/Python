# Dicionário de contas vazio
contas = {}

# Solicitar ao usuário o nome da conta
conta = input("Digite o nome da conta: ")

# Solicitar ao usuário o limite de gastos
limite_gastos = float(input("Digite o limite de gastos da conta: "))

# Inicializar a conta no dicionário
contas[conta] = {'saldo_devedor': 0, 'numero_transacoes': 0, 'media_gastos': 0, 'limite_gastos': limite_gastos}

while True:
    # Solicitar ao usuário o valor da compra
    valor_compra = float(input("Digite o valor da compra (ou 0 para sair): "))

    # Verificar se o usuário deseja sair
    if valor_compra == 0:
        break

    # Atualizar o saldo devedor
    contas[conta]['saldo_devedor'] += valor_compra

    # Atualizar o número de transações
    contas[conta]['numero_transacoes'] += 1

    # Atualizar a média de gastos
    novo_saldo = contas[conta]['saldo_devedor']
    novo_numero_transacoes = contas[conta]['numero_transacoes']
    contas[conta]['media_gastos'] = novo_saldo / novo_numero_transacoes

    # Calcular o saldo disponível
    saldo_disponivel = contas[conta]['limite_gastos'] - contas[conta]['saldo_devedor']

    # Exibir o saldo disponível e se a pessoa está positiva ou negativa
if saldo_disponivel >= 0:
        print(f"Saldo disponível: R${saldo_disponivel:.2f} (Positivo)")
else:
        print(f"Saldo disponível: R${saldo_disponivel:.2f} (Negativo)")