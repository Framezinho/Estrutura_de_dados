from No import No

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo
        self.fim = nodo
        print(f"\nAdicionado: {valor}")
        self.imprimir()

    def imprimir(self):
        print("\n----------------------")
        print("Fila - FIFO")

        if self.inicio is None:
            print("Fila Vazia")
            return

        aux = self.inicio
        elementos = []
        while aux:
            elementos.append(str(aux.dado))
            aux = aux.prox
        print(" -> ".join(elementos))

    def remover(self):
        if self.inicio is None:
            print("\nFila Vazia. Nada para remover.")
            return None

        valor = self.inicio.dado
        self.inicio = self.inicio.prox
        if self.inicio is None:
            self.fim = None

        print(f"\nRemovido: {valor}")
        self.imprimir()
        return valor