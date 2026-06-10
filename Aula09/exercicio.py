def por_extenso(numero):
    tupla = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")
    try:
        n = int(numero)
    except Exception:
        raise ValueError("Entrada não valida: deve ser um numero inteiro de 0 a 9")
    if not 0 <= n <= 9:
        raise ValueError("Numero fora de 0-9")
    return tupla[n]

def criar_aluno(nome, nota01, nota02):

    try:
        n1 = float(nota01)
        n2 = float(nota02)
    except Exception:
        raise ValueError("Notas invalidas: devem ser numeros")
    final = (n1 + n2) / 2
    aluno = {
        "nome": nome,
        "nota01": n1,
        "nota02": n2,
        "final": final,
    }
    return aluno


def main():
    print("Escolha a opção: 1 - Numero por extenso | 2 - Dados do aluno")
    opc = input("Opção (1/2): ")
    if opc == "1":
        num = input("Digite um numero de 0 a 9: ")
        try:
            print(f"Resultado: {por_extenso(num)}")
        except ValueError as e:
            print(e)
    elif opc == "2":
        nome = input("Nome do aluno: ")
        n1 = input("Nota 01: ")
        n2 = input("Nota 02: ")
        try:
            aluno = criar_aluno(nome, n1, n2)
            print("Dados do aluno:")
            for k, v in aluno.items():
                print(f"{k}: {v}")
        except ValueError as e:
            print(e)
    else:
        print("Opção invalidas. Saindo.")


if __name__ == "__main__":
    main()
