class OrganizadorFinanceiro:
    def __init__(self):
        self.despesas = []

    def adicionar_despesa(self, descricao, valor):
        self.despesas.append({"descricao": descricao, "valor": valor})

    def calcular_total(self):
        total = 0
        for despesa in self.despesas:
            total += despesa["valor"]
        return total

    def listar_despesas(self):
        for despesa in self.despesas:
            print(f"{despesa['descricao']}: R$ {despesa['valor']}")


def main():
    organizador = OrganizadorFinanceiro()
    while True:
        print("Organizador Financeiro")
        print("---------------------")
        print("1. Adicionar despesa")
        print("2. Calcular total de despesas")
        print("3. Listar despesas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Digite a descrição da despesa: ")
            valor = float(input("Digite o valor da despesa: "))
            organizador.adicionar_despesa(descricao, valor)
            print("Despesa adicionada com sucesso!")
            print()

        elif opcao == "2":
            total = organizador.calcular_total()
            print(f"Total de despesas: R$ {total}")
            print()

        elif opcao == "3":
            print("Despesas:")
            organizador.listar_despesas()
            print()

        elif opcao == "4":
            print("Encerrando o Organizador Financeiro...")
            break

        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")
            print()


if __name__ == "__main__":
    main()
