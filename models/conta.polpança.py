from .conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo=0):
        super().__init__(titular, saldo)
        self.cofrinho = 0

    def guardar_no_cofrinho(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.cofrinho += valor

    def tirar_do_cofrinho(self, valor):
        if valor <= self.cofrinho:
            self.cofrinho -= valor
            self.saldo += valor

    def to_dict(self):
        d = super().to_dict()
        d["cofrinho"] = self.cofrinho
        return d
