from repository.banco_de_dados import BancoDados
from models.conta import Conta
from models.conta_corrente import ContaCorrente

db = BancoDados()

def listar(contas):
    print("\n--- LISTA DE CONTAS ---")
    for c in contas:
        print(f"{c.numero} - {c.titular} - Saldo: {c.saldo}")

def criar_conta(contas):
    tipo = input("Tipo [1] Conta | [2] Conta Corrente: ")

    numero = input("Número da conta: ")
    titular = input("Titular: ")
    saldo = float(input("Saldo inicial: "))

    if tipo == "2":
        limite = float(input("Limite: "))
        contas.append(ContaCorrente(numero, titular, saldo, limite))
    else:
        contas.append(Conta(numero, titular, saldo))

    print("Conta criada com sucesso!")

def editar(contas):
    numero = input("Número da conta para editar: ")
    for c in contas:
        if c.numero == numero:
            novo_titular = input("Novo titular: ")
            c.titular = novo_titular
            print("Conta atualizada!")
            return
    print("Conta não encontrada.")

def remover(contas):
    numero = input("Número da conta para remover: ")
    for c in contas:
        if c.numero == numero:
            contas.remove(c)
            print("Conta removida!")
            return
    print("Conta não encontrada.")

def main():
    contas = db.carregar()

    while True:
        print("\n--- MENU ---")
        print("1 - Listar")
        print("2 - Criar conta")
        print("3 - Editar conta")
        print("4 - Remover conta")
        print("5 - Salvar e sair")

        opc = input("Escolha: ")

        if opc == "1":
            listar(contas)

        elif opc == "2":
            criar_conta(contas)

        elif opc == "3":
            editar(contas)

        elif opc == "4":
            remover(contas)

        elif opc == "5":
            db.salvar(contas)
            print("Dados salvos! Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
