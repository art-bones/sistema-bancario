from banco_dados import*

#adicionar valor implementado na propria função
def depositar(conta):
    valor = int(input("Digite o valor a ser deposita: "))
    if valor <= 0:
        print("O valor do depósito deve ser maior que zero.")
        return
    conta.saldo += valor
    conta.extrato.append(f"Depósito: +{valor}")
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {conta.saldo:.2f}")

#adicionar valor implementado na propria função
def sacar(conta):
    if conta.saques_diarios >= conta.limite_saques_diarios:
        print("Você atingiu o limite diário de saques.")
        return
    valor = int(input("Digite o valor a ser sacado: "))
    if valor > 500:
        print("O valor do saque deve ser no máximo R$ 500.")
        return
    if conta.saldo - valor < 0:
        print("Saldo insuficiente para realizar o saque.")
        return
    if valor <= 0:
        print("O valor do saque deve ser maior que zero.")
        return
    conta.saldo -= valor
    conta.saques_diarios += 1
    conta.extrato.append(f"Saque: -{valor}")
    print(f"Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {conta.saldo:.2f}")


def mostrar_extrato(conta):
    print("Extrato bancário:")
    for operacao in conta.extrato:
        print(operacao)
    print(f"Saldo atual: R$ {conta.saldo:.2f}")    

  
class Usuario:
    def __init__(self, nome, nascimento, cpf, endereço):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.endereço = endereço
    def __str__(self):
        return f"nome: {self.nome} nascimento: {self.nascimento} cpf: {self.cpf} endereço {self.endereço}"   

#adicionar verificações e tratativas de erros
def cadastrar_usuario():
    nome = input("Digite o nome do titular: ")
    nascimento = int(input("Digite a data de nascimento do titular: "))
    cpf = int(input("Digite o cpf do titular: "))
    endereço = input("Digite o endereço do titular: ")
    novo_usuario = Usuario(nome=nome, nascimento=nascimento, cpf=cpf, endereço=endereço)
    lista_usuarios.append(novo_usuario)
    print("Usuario cadastrado com sucesso")
    return novo_usuario

#adicionar verificações e tratativas de erros
def buscar_usuario_por_cpf():
    cpf = int(input("Digite o cpf do titular: "))
    for usuario in lista_usuarios:
        if usuario.cpf == cpf:
            print(usuario)
            return cpf
    return None


#testar retornos adequados das informações da conta
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

#adicionar verificações e tratativas de erros, consertar o print com o número da conta
def criar_conta():
    global numero_conta_atual
    numero_conta_atual += 1
    numero_conta = f'{numero_conta_atual:06}'
    usuario = buscar_usuario_por_cpf() 
    nova_conta = Conta(numero=numero_conta, usuario=usuario)
    contas[numero_conta] = nova_conta
    print("Conta de número  criada com sucesso!")
    return nova_conta

#adicionar verificações e tratativas de erros
def obter_conta(numero_conta):
    return contas.get(numero_conta)

