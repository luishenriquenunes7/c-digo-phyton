Exercício 1.2

def menu():
    print("\n--- Bilheteria de Evento ---")
    print("1 - Cadastrar nome do evento")
    print("2 - Vender ingressos")
    print("3 - Repor ingressos")
    print("4 - Ver ingressos disponiveis")
    print("0 - Sair")
    return input("Escolha uma opção: ")
    
    
    #Variáveis de Controle
evento = None
quantidade = 0

while True:
    opcao = menu()
    
    if opcao == "1":
       evento = input("Qual evento você deseja ir? : ")
       quantidade = 1
       print(f"Evento '{evento}' Cadastrado com sucesso! ")
       
    elif opcao == "2":
      if evento is None:
          print("Nenhum evento cadastrado ainda! ")
      else:
            vender = int(input("Quantos ingressos deseja vender? :"))
            quantidade = 2
            if vender <= 0:
                print("A quantidade deve ser maior que zero!")
            elif vender > quantidade:
                print("Não há ingressos suficientes!")
            else:
                quantidade -= vender
                print(f"Vendido {vender}unidade(s). Quantidade de ingresso atual:{quantidade}")
                
    elif opcao == "3":
        if evento is None:
           print("Nenhum evento cadastrado ainda!")
        else:
            repor = int(input("Digite a quantidade de ingressos que deseja repor: "))
            quantidade = 3
            if repor <= 0:
                print("A quantidade deve ser maior que zero!")
            else:
                quantidade += repor
                print(f"Adicionado{repor}unidade(s). Quantidade de ingresso no estoque : {quantidade}")
                
    elif opcao == "4":
        if evento is None:
            print("Nenhum evento cadastrado ainda!")
        else:
            ingresso = print("Ver ingressos disponiveis" ))
            quantidade = 5 
            if ingresso <= 0: