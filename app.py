import json
from models.conta_corrente import ContaCorrente
from models.conta_poupanca import ContaPoupanca

CAMINHO = "data/contas.json"

# Salvar

def salvar(contas):
    with open(CAMINHO, "w", encoding="utf-8") as arq:
        json.dump([c.to_dict() for c in contas], arq, indent=4)

# Carregar

def carregar():
    try:
        with open(CAMINHO, "r", encoding="utf-8") as arq:
            dados = json.load(arq)
    except FileNotFoundError:
        return []

    contas = []
    for item in dados:
        if item["tipo"] == "ContaCorrente":
            contas.append(ContaCorrente(item["titular"], item["saldo"], item["limite"]))
        else:
            cp = ContaPoupanca(item["titular"], item["saldo"])
            cp.cofrinho = item.get("cofrinho", 0)
            contas.append(cp)
    return contas

# Exemplo de uso
cc = ContaCorrente("Maria", 1000)
cp = ContaPoupanca("João", 500)

cc.sacar(1200)       # usa limite
cp.guardar_no_cofrinho(100)
cp.tirar_do_cofrinho(50)

salvar([cc, cp])

for conta in carregar():
    conta.extrato()
