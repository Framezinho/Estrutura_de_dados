from Arvore import Arvore

a = Arvore()

a.inserir(a.raiz, 50)
a.inserir(a.raiz, 60)
a.inserir(a.raiz, 40)
a.inserir(a.raiz, 5)
a.inserir(a.raiz, 55)

a.imprimirEmOrdem(a.raiz)
print("\n")
a.imprimirEmOrdem(a.raiz.esq)