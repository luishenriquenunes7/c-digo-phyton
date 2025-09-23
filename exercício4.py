Exercício 4

from dataclasses import dataclass
from datetime import datetime
#criando uma classe de publicação.classe é um modelo que define atributos(características)e métodos(ações).
@dataclass
class Publicacao:
    conteudo:str
    descricao:str
    autor:str
    data_hora: datetime
    curtidas: int = 0
#criando uma variável lista.lista é uma variável que se pode armazenar varias informações.
lista_publicacoes = []
#criando uma função para a classe "Publicacao",esta função serve para criar a publicacao,(def:usado para definir funções,print:exibir a mensagem escolhida,input:serve para obter dados a partir da linha de comando)
def criar_publicacao():
    print("\n=== CRIAR PUBLICAÇÃO ===")
    conteudo = input("Digite o conteúdo da publicação: ")
    descricao = input("Digite a descrição: ")
    autor = input("Digite o nome do autor: ")
    data_hora = datetime.now()
    
    nova_publicacao = Publicacao(conteudo, descricao, autor, data_hora)
    lista_publicacoes.append(nova_publicacao)
    print ("Publicação criada com sucesso!")
#criando uma função para a classe "Publicacao",esta função serve para curtir a publicação,(if not:usado para verificar a ausência de um valor ou de uma situação).
def curtir_publicacao():
    print("\n=== CURTIR PUBLICAÇÃO ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
#mostra todas as publicações disponíveis
    visualizar_feed()
    try:
        indice = int(input("Digite o número da publicação para curtir: ")) -1
        if 0 <= indice < len(lista_publicacoes):
            lista_publicacoes[indice].curtidas += 1
            print("Publicação curtida!")
        else:
            print("Publicação não encontrada.")
    except ValueError:
        print("Número inválido.")
#função para exibir todas as publicações em ordem
def visualizar_feed():
    print("\n=== FEED ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    
    for i,pub in enumerate(lista_publicacoes,1):
        print(f"(i). {pub.autor} - {pub.curtidas} curtidas")
        print(f" {pub.conteudo[:50]}...")
        print(f" {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
        print("-" * 40)
 #função para visualizar uma publicação completa (individual)       
def visualizar_publicacao_individual():
    print("\n=== VISUALIZAR PUBLICAÇÃO ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    
    visualizar_feed()
    try:
        indice = int(input("Digite o número da publicação: ")) -1
        if 0 <= indice < len(lista_publicacoes):
            pub = lista_publicacoes[indice]
            print(f"\nAutor: {pub.autor}")
            print(f"Data: {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
            print(f"Conteúdo: {pub.conteudo}")
            print(f"Descrição: {pub.descricao}")
            print(f"Curtidas: {pub.curtidas}")
        else:
            print("Publicação não encontrada.")
    except ValueError:
        print("Número inválido.")
 #função para visualizar uma publicações de um autor específico  
def visualizar_publicacoes_por_autor():
    print("\n=== PUBLICAÇÕES POR AUTOR ===")
    if not lista_publicacoes:
        print("Nenhuma publicação disponível.")
        return
    
    autor = input("Digite o nome do autor: ")
    publicacoes_autor = [pub for pub in lista_publicacoes if pub.autor.lower() == autor.lower()]
    
    if not publicacoes_autor:
        print(f"Nenhuma publicação encontrada para {autor}.")
        return
    
    print(f"\nPublicações de {autor}:")
    for pub in publicacoes_autor:
        print(f"- {pub.conteudo[:50]}...({pub.curtidas} curtidas)")
        print(f"  {pub.data_hora.strftime('%d/%m/%Y %H:%M')}")
        print("-" * 30)
 #função principal (menu do sistema)      
def menu():
    while True:
        print("\n=== REDE SOCIAL ===")
        print("1. Criar Publicação")
        print("2. Curtir Publicação")
        print("3. Visualizar Feed")
        print("4. Visualizar Publicação Individual")
        print("5. Visualizar Publicações por Autor")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            criar_publicacao()
        elif opcao == "2":
            curtir_publicacao()
        elif opcao == "3":
            visualizar_feed()
        elif opcao == "4":
            visualizar_publicacao_individual()
        elif opcao == "5":
            visualizar_publicacoes_por_autor()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
            
if __name__ == "__main__":
    menu()
        
        

        
