from banco_dados import*   
 
class Usuario:
    def __init__(self, nome, nascimento, cpf, endereço):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.endereço = endereço
    def __str__(self):
        return f"nome: {self.nome} nascimento: {self.nascimento} cpf: {self.cpf} endereço: {self.endereço}"   

#adicionar verificações e tratativas de erros
def cadastrar_usuario():
    nome = input("Digite o nome do titular: ")
    nascimento = int(input("Digite a data de nascimento do titular: "))
    cpf = int(input("Digite o cpf do titular: "))
    endereço = input("Digite o endereço do titular: ")
    novo_usuario = Usuario(nome=nome, nascimento=nascimento, cpf=cpf, endereço=endereço)
    lista_usuarios.append(novo_usuario)
    print("Usuario cadastrado com sucesso")
    return

#adicionar verificações e tratativas de erros
def buscar_usuario_por_cpf():
    cpf = int(input("Digite o cpf do titular: "))
    for Usuario in lista_usuarios:
        if Usuario.cpf == cpf:
            print(Usuario)
            return cpf
    print("Usuario não encontrado ou cpf inválido, por favor tente novamente")
    return None

class Conta:
    def __init__(self, numero, usuario):
        self.numero = numero
        self.agencia = 1
        self.usuario = usuario
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0
        self.limite_saques_diarios = 3
    def __str__(self):
        return f"{self.saldo}"
           
    def depositar(self):
     valor = int(input("Digite o valor a ser deposita: "))
     if valor <= 0:
        print("O valor do depósito deve ser maior que zero.")
        return
     self.saldo += valor
     self.extrato.append(f"Depósito: +{valor}")
     print(f"Depósito de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}")

    def sacar(self):
     if self.saques_diarios >= self.limite_saques_diarios:
        print("Você atingiu o limite diário de saques.")
        return
     valor = int(input("Digite o valor a ser sacado: "))
     if valor > 500:
        print("O valor do saque deve ser no máximo R$ 500.")
        return
     if self.saldo - valor < 0:
        print("Saldo insuficiente para realizar o saque.")
        return
     if valor <= 0:
        print("O valor do saque deve ser maior que zero.")
        return
     self.saldo -= valor
     self.saques_diarios += 1
     self.extrato.append(f"Saque: -{valor}")
     print(f"Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}")

    def mostrar_extrato(self):
     print("Extrato bancário:")
     for operacao in self.extrato:
        print(operacao)
     print(f"Saldo atual: R$ {self.saldo:.2f}")  

#adicionar verificações e tratativas de erros, consertar o print com o número da conta
def criar_conta():
    global numero_conta_atual
    numero_conta_atual += 1
    numero_conta = f'{numero_conta_atual:06}'
    usuario = buscar_usuario_por_cpf() 
    nova_conta = Conta(numero=numero_conta, usuario=usuario)
    contas[numero_conta] = nova_conta
    print (f"Conta de número {nova_conta.numero} criada com sucesso")
    return


def obter_conta(numero):
    return contas.get(numero)

