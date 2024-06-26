import textwrap
import time
from datetime import datetime
from pathlib import Path

ROOT_PATH = Path(__file__).parent


class ContasInterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""
                Agência: {conta.agencia}
                Saldo atual: R$ {conta.saldo: .2f}
                Número: {conta.numero}
                Titular: {conta.cliente.nome}
            """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("Você excedeu o limite de transações permitidas")
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

        def __repr__(self) -> str:
            return f"<{self.__class__.__name__}: ('{self.cpf}')"


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque!!!")
            return False

        if valor > self.saldo:
            print("Saldo insuficiente para saque!!!")
            return False

        self._saldo -= valor
        print("Saque realizado com sucesso")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito!!!")
            return False

        self._saldo += valor
        print("Depósito realizado!!!")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque!!!")
            return False

        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        if valor > self.limite:
            print("Valor excede o limite de saque!!!")
            return False

        if numero_saques >= self.limite_saque:
            print("Limite de saques excedido!!!")
            return False

        if valor > self.saldo:
            print("Saldo insuficiente para saque!!!")
            return False

        self._saldo -= valor
        print("Saque realizado com sucesso")
        return True

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"

    def __str__(self):
        return f"""
            Agência: {self.agencia}
            Numero: {self.numero}
            Titular: {self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "Valor": transacao.valor,
                "Data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if (
                tipo_transacao is None
                or transacao["tipo"].lower() == tipo_transacao.lower()
            ):
                yield transacao

    def transacoes_do_dia(self):
        data_atual = datetime.now().date()
        transacoes = []
        for transacao in self.transacoes:
            data_transacao = datetime.strptime(
                transacao["Data"], "%d-%m-%Y %H:%M:%S"
            ).date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes


class Transacao:
    @property
    def valor(self):
        pass

    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        data_hora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        try:
            with open(
                ROOT_PATH / "log.txt", "a", newline="", encoding="utf-8"
            ) as arquivo:
                arquivo.write(
                    f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}. retornou {resultado} \n"
                )
        except IOError as exc:
            print(f"Erro ao carregar arquivo {exc}")
        return resultado

    return envelope


def menu():
    menu = """  
        BEM VINDO AO NOSSO BANCO
    [u] Criar cliente
    [nc] Nova Conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [l] Listar Contas
    [q] Sair
    => """
    return input(menu)


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta")
        return None

    return cliente.contas[0]


@log_transacao
def depositar(clientes):
    cpf = input("Insira seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return

    valor = float(input("Informe o valor para depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    transacao.registrar(conta)


@log_transacao
def sacar(clientes):
    cpf = input("Insira seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return

    valor = float(input("Insira o valor para saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    transacao.registrar(conta)


@log_transacao
def exibir_extrato(clientes):
    cpf = input("Insira seu CPF: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("########################## EXTRATO ##########################")
    transacoes = conta.historico.gerar_relatorio()

    if not transacoes:
        print("Não foram feitas movimentações")
    else:
        for transacao in transacoes:
            print(
                f"{transacao['Data']} {transacao['tipo']}: R$ {transacao['Valor']:.2f}"
            )
    print(f"Saldo: R$ {conta.saldo:.2f}")
    print("#############################################################")


@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Cliente já existente com este CPF")
        return

    nome = input("Digite seu nome: ")
    data_nascimento = input("Informe a sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (cidade - estado): ")

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
    )
    clientes.append(cliente)
    print("Cliente criado com sucesso")


@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe seu CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("Cliente não cadastrado")
        return

    conta = ContaCorrente(numero=numero_conta, cliente=cliente)
    contas.append(conta)
    cliente.adicionar_conta(conta)

    print("Conta criada com sucesso")


def listar_contas(contas):
    for conta in ContasInterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    contas = []
    clientes = []

    while True:
        opcao = menu()

        if opcao == "u":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por utilizar nosso Sistema, até logo :)")
            time.sleep(1)
            break

        else:
            print("Operação inválida")


main()
