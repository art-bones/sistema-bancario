from banco_dados import*   
 #Estrutura da classe Usuario, com as informações para cadastro do cliente.
class Usuario:
    def __init__(self, nome, nascimento, cpf, endereço):
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf
        self.endereço = endereço
    def __str__(self):
        return f"nome: {self.nome} nascimento: {self.nascimento} cpf: {self.cpf} endereço: {self.endereço}"   

#Função para a criação de uma instancia de Usuario, que será armazenado em uma lista em outro arquivo simulando um bando de dados.
#Próxima fase inclui mecanismos de verificação de que as informações atendem ao padrão de négocios e tratamento de erros em caso de informações inadequadas
def cadastrar_usuario():
    nome = input("Digite o nome do titular: ")
    nascimento = int(input("Digite a data de nascimento do titular: "))
    cpf = int(input("Digite o cpf do titular: "))
    endereço = input("Digite o endereço do titular: ")
    novo_usuario = Usuario(nome=nome, nascimento=nascimento, cpf=cpf, endereço=endereço)
    lista_usuarios.append(novo_usuario)
    print("Usuario cadastrado com sucesso")
    return

#Função que pecorre a lista de clientes procurando por um cpf em específico, é tambem usada na função de crianção de conta.
#Proxima fase inclui mecanismo de verificação de que as informações recebidas e retornadas atendam ao padrão de negócio
def buscar_usuario_por_cpf():
    cpf = int(input("Digite o cpf do titular: "))
    for Usuario in lista_usuarios:
        if Usuario.cpf == cpf:
            print(Usuario)
            return cpf
    print("Usuario não encontrado ou cpf inválido, por favor tente novamente")
    return None
#Declaração da estrutura de uma conta, atendendo as especificações demandadas. Tambem a maioria das funcionalidades de manipulação de uma conta foram implementadas como métodos
#Proxima fase terá mais funcionalidades para manipular a conta
class Conta:
    def __init__(self, numero, usuario_cpf):
        self.numero = numero
        self.agencia = 1
        self.usuario_cpf = usuario_cpf
        self.saldo = 0
        self.extrato = []
        self.saques_diarios = 0
        self.limite_saques_diarios = 3

    def get_saldo(self):
       return self.saldo
           
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

#Função que cria uma conta, criando seu número automaticamente e à associando a um cliente pré-cadastrado e armazenando em um dicionário simulando um banco de dados.
#Próximo passo incluí tratamento de erros caso o usuário não esteja cadastrado por exemplo.
def criar_conta():
    global numero_conta_atual
    numero_conta_atual += 1
    numero_conta = f'{numero_conta_atual:06}'
    usuario_cpf = buscar_usuario_por_cpf() 
    nova_conta = Conta(numero=numero_conta, usuario_cpf=usuario_cpf)
    if usuario_cpf not in contas:
       contas[usuario_cpf] = []
    contas[usuario_cpf].append(nova_conta)
    print (f"Conta de número {nova_conta.numero} criada com sucesso")
    return

#Função que recebe um número de conta e percorre o armazenamento de contas para ferificar se tal conta existe, e posteriormente devolve a conta. Utilizado para acessar uma instancia de conta específica.
def obter_conta(numero):
    for usuario_cpf in contas:
        for conta in contas[usuario_cpf]:
            if conta.numero == numero:
                return conta
    return False

