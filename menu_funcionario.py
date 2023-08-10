# arquivo: main.py
from operacoes import obter_conta, criar_conta, cadastrar_usuario, buscar_usuario_por_cpf, Conta

tentativas = 3
def main():
    global tentativas
    while tentativas > 0:
        print("\nOpções:")
        print("1. Cadastrar usuario")
        print("2. Buscar usuario")
        print("3. Criar conta")
        print("4. Acessar conta")
        print("5. Sair")

        escolha = input("Escolha uma opção (1/2/3/4/5): ")

        if escolha == "1":        
            cadastrar_usuario()

        elif escolha == "2":        
            buscar_usuario_por_cpf()

        elif escolha == "3":        
            criar_conta()  

        elif escolha == "4":
            numero = input("Digite o número da conta: ")
            conta = obter_conta(numero)
            if conta:
                interagir_com_conta(conta)
            else:
                tentativas -= 1
                print("Conta não encontrada.")

        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def interagir_com_conta(conta):
    while True:
        print("Saldo atual: R$ ")
        print("\nOpções:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Mostrar extrato")
        print("4. Voltar")

        escolha = input("Escolha uma opção (1/2/3/4): ")

        if escolha == "1":
            conta.depositar()
        elif escolha == "2":
            conta.sacar()
        elif escolha == "3":
            conta.mostrar_extrato()
        elif escolha == "4":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")        

if __name__ == "__main__":
    main()
