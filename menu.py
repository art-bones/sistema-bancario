# arquivo: main.py
from operacoes import sacar, depositar, mostrar_extrato, obter_conta, criar_conta, cadastrar_usuario, buscar_usuario_por_cpf

def main():
    while True:
        print("\nOpções:")
        print("1. Cadastrar usuario")
        print("2. Buscar")
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
            numero_conta = input("Digite o número da conta: ")
            conta = obter_conta(numero_conta)
            if conta:
                interagir_com_conta(conta)
            else:
                print("Conta não encontrada.")

        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def interagir_com_conta(conta):
    while True:
        print("Saldo atual: R$ {conta.saldo}")
        print("\nOpções:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Mostrar extrato")
        print("4. Voltar")

        escolha = input("Escolha uma opção (1/2/3/4): ")

        if escolha == "1":
            depositar(conta)
        elif escolha == "2":
            sacar(conta)
        elif escolha == "3":
            mostrar_extrato(conta)
        elif escolha == "4":
            print("Voltando ao menu principal...")
            break
        else:
            print("Opção inválida. Tente novamente.")        

if __name__ == "__main__":
    main()
