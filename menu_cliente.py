from menu_funcionario import interagir_com_conta
from operacoes import obter_conta

tentativas = 3
def main():
 global tentativas   
 while tentativas > 0:    
    numero = input("Digite o número da conta: ")
    conta = obter_conta(numero)
    if conta:
     interagir_com_conta(conta)
    else:
     tentativas -= 1   
     print("Conta não encontrada.")

if __name__ == "__main__":
    main()