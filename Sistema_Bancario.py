menu="Menu"

print(menu.center(8,"*"))

print('''
 [d] Depósito;
 [s] Saque;
 [e] Extrato;
 [q] Sair do sistema.
''')
      
saldo=0
extrato=''
Qtdade_saques=0
limiteSaque=500
NumeroSaques=3

while True:

    opcao=input("Selecione uma opção: ")

    if opcao=="d":
        valor=float(input("Qual o valor do depósito?: "))
        if valor>0:
            saldo+=valor
            extrato+=f"Depósito: R$ {valor:.2f}\n"
        else:
            print("O valor informado é inválido")

    elif opcao=="s":
        valorSaque=float(input("Qual o valor do saque?: "))

        if (Qtdade_saques<NumeroSaques) and (valorSaque<=limiteSaque) and (valorSaque<=saldo) and (valorSaque>0):
            saldo-=valorSaque
            Qtdade_saques+=1
            extrato+=f"Saque: R${valorSaque:.2f}\n"

        elif Qtdade_saques>=NumeroSaques:
            print(Qtdade_saques)
            print("Número de saques excedido!")

        elif valorSaque>limiteSaque:
            print("Valor superior ao limte de R$500!")

        elif valorSaque>saldo:
            print("Saldo insuficiente!")
        
        elif valorSaque<0:
            print("Valor inválido!")
    
    elif opcao=="e":
        print("\n--------------EXTRATO--------------")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n-----------------------------------")
    
    elif opcao=="q":
        break
    else:
        print('''Opção inválida. Por favor, selecione uma opção do menu
           
           **Menu**
           
         [d] Depósito;
         [s] Saque;
         [e] Extrato;
         [q] Sair do sistema.
        ''')
