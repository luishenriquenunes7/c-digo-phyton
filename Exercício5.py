Exercício 5

#requisitos
1- o Cliente deverá informar seu nome e sobrenome.

2- o Cliente deverá fazer um login no site com seu e-mail.

3- o Cliente deverá escolher o serviço que está procurando(Corte,Barba,Corte e barba e sobrancelha).
 
4- o Cliente deverá agendar o dia e o horário.

5- o Cliente deverá escolher o barbeiro,de acordo com o dia e o horário escolhido.

6- o Cliente deverá informar a forma de pagamento.

7- Após o agendamento,o cliente deverá deixar seu número de telefone para um lembrete Via WhatsApp.

8- Após o Cliente concluir o agendamento,na mesma hora será mandado um e-mail de confirmação.

9- Após o agendamento ser realizado,o cliente poderá agendar um novo corte ou ver seus agendamentos já feitos.

10- Deverá ter um histórico de cada agendamento feito por clientes.

11- Se algum cliente desmarcar,o horário marcado deve ser restaurado.

@dataclass
class Cliente:
    nome:str
    celular:str
    email:str
    
@dataclass
class Barbeiro:
    nome:str
    disponibilidade:str
    horario:str
    serviço:str
    
lista_barbeiros = ["Gustavo", "Lucas", "Breno"]
@dataclass
class Agendamento:
    data:str
    hora:str
    barbeiro:str
    
lista_horarios = ["10h", "11h", "14h", "15h30", "16h"]
@dataclass
class Serviços:
    corte:str
    barba:str
    corte e barba:str
    sobrancelha:str
    
lista_serviços = ["corte", "barba", "sobrancelha"]

@dataclass
class Pagamentos:
    pix:str
    crédito:str
    débito:str
    dinheiro:str

lista_pagamentos = ["pix", "crédito", "débito", "dinheiro"]    

def agendar():
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    barbeiro = input("Escolha seu barbeiro: ")
    data = input("Qual data deseja?: ")
    hora = input("Escolha a Hora desejada: ")
    pagamento = input("Escolha a forma de pagamento: ")
    celular = input("Qual seu contato?: ")
    cliente_digitado = cliente(nome,email,celular)
    lista.append(cliente_digitado)
    print("Cadastro realizado com sucesso")
    
def menu():
    print("1 - Cadastrar agendamento")
    print("2 - Ver serviços")
    print("3 - Preço do serviço ")
    print("4 - Ver horario disponivel")
    print("5 - Ver clientes cadastrados")
    print("6 - Sair")
    return input("Escolha uma opção: ")
#variaveis de controle


while True:
    opcao = menu()
        
    if opcao == "1":
        nome = input("Nome do cliente: ")
       celular = input("Inserir contato: ")
        email = input("Digite seu email: ")
        cliente = Cliente(nome,contato,email)
        lista_pessoas.append(cliente)
        data = input("Inserir data: ")
        hora = input("Digite o horário: ")
        barbeiro = input("Escolha seu barbeiro: ")
        servico = input("Tipo de serviço: ")
        agendamento = Agendamento(data,hora,barbeiro)
        pagamento = input("Escolha a forma de pagamento: ")
        lista_serviços.append(agendamento)    
        print(f"agendamento '{agendamento}' agendado com sucesso!")
        
    if opcao == "2":
        print("\n--- Serviços ---")
        
        print("\n--- Cortes ---")
        for servico in lista_cortes:
            print(f"- {servico}")
        
        print("\n--- Barbas ---")
        for servico in lista_barba:
            print(f"- {servico}")
            
        print("\n--- Sobrancelhas ---")
        for servico in lista_sombrancelha:
            print(f"- {servico}")
            
        print("----------------------------")
        
    if opcao == "3":
        valor_do_corte=40
        print(f"O valor do corte é R$ {valor_do_corte},00")
        valor_da_barba=20
        print(f"O valor da barba é R$ {valor_da_barba},00")
        valor_da_sobrancelha=10
        print(f"O valor da sobrancelha é R$ {valor_da_sobrancelha},00")
        
    if opcao == "4":
        print("Horários disponíveis: ")
        for horario in lista_horarios:
            print(horario)
        escolher = input("Escolha o horário: ")
        if escolher in lista_horarios:
            print(f"Você escolheu o horário {escolher}. Agendamento feito!")
            
    if opcao == "5":
        print("\n--- Ver clientes cadastrados ---")
        if not lista_pessoas:
            print("Ainda não há clientes cadastrados!")
        else:
            for cliente in lista_pessoas:
                print(f" {cliente}")
                
        print("Esses são os clientes cadastrados.")
        
    if opcao == "6":
        print("Obrigado pela atenção!")
        
    break

