from .conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo=0, limite=500):
        super().__init__(numero, titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return True
        return False

    def to_dict(self):
        data = super().to_dict()
        data["tipo"] = "ContaCorrente"
        data["limite"] = self.limite
        return data