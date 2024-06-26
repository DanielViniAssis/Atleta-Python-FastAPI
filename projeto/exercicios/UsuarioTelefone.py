class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def fazer_chamada(self, destinatario, duracao):
        custo_chamada = self.plano.custo_chamada(int(duracao))
        if self.plano.verificar_saldo() >= custo_chamada:
            self.plano.deduzir_saldo(custo_chamada)
            self.destinatario = destinatario
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${float(self.plano.verificar_saldo()):.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."


class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def verificar_saldo(self):
        return self.saldo

    def custo_chamada(self, duracao):
        return 0.10 * duracao

    def deduzir_saldo(self, deduzir):
        self.saldo -= deduzir


class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


nome = input()
numero = input()
saldo_inicial = float(input())

usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = input()

print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
