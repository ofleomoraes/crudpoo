class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        return False

    def to_dict(self):
        return {
            "tipo": "Conta",
            "numero": self.numero,
            "titular": self.titular,
            "saldo": self.saldo
        }
