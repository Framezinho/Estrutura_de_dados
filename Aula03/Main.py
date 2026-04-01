from Fila import Fila


def menu():
    fila = Fila()

    while True:
        print("\n=== Menu de Filas (Aula03) ===")
        print("1) Inserir na fila")
        print("2) Remover da fila")
        print("3) Exibir fila")
        print("4) Limpar fila")
        print("0) Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            valor = input("Digite o valor a inserir: ").strip()
            if valor:
                fila.add(valor)
            else:
                print("Valor inválido. Tente novamente.")

        elif opcao == "2":
            fila.remover()

        elif opcao == "3":
            fila.imprimir()

        elif opcao == "4":
            fila.inicio = None
            fila.fim = None
            print("Fila limpa.")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()