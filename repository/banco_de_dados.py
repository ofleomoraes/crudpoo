import json
import os
from models.conta import Conta
from models.conta_corrente import ContaCorrente

CAMINHO_ARQUIVO = "data/contas.json"

class BancoDados:
    def __init__(self):
        if not os.path.exists("data"):
            os.makedirs("data")

        if not os.path.exists(CAMINHO_ARQUIVO):
            with open(CAMINHO_ARQUIVO, "w") as f:
                json.dump([], f)

    def carregar(self):
        with open(CAMINHO_ARQUIVO, "r") as f:
            dados = json.load(f)

        contas = []
        for c in dados:
            if c["tipo"] == "ContaCorrente":
                contas.append(
                    ContaCorrente(c["numero"], c["titular"], c["saldo"], c["limite"])
                )
            else:
                contas.append(
                    Conta(c["numero"], c["titular"], c["saldo"])
                )

        return contas

    def salvar(self, contas):
        dados = [c.to_dict() for c in contas]
        with open(CAMINHO_ARQUIVO, "w") as f:
            json.dump(dados, f, indent=4)
