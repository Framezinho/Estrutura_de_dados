from Arvore import Arvore

a = Arvore()

a.inserir(a.raiz, 48)
a.inserir(a.raiz, 97)
a.inserir(a.raiz, 51)
a.inserir(a.raiz, 63)
a.inserir(a.raiz, 22)
a.inserir(a.raiz, 44)
a.inserir(a.raiz, 21)
a.inserir(a.raiz, 14)
a.inserir(a.raiz, 5)


a.imprimirEmOrdem(a.raiz)
print("\n")
a.imprimirEmOrdem(a.raiz.esq)


