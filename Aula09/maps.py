def imprimirNone(n ) :
    print("none: ", n)
    nones = "João", "Maria", "Pedro"

    resultNomes = map(imprimirNone, nones)
    list(resultNomes)

    print("--------------------")

    def aumentarPreco(preco):
        return preco * 1.1  
    
precos = [100, 200, 300, 400, 500]
print("Preços antigos:", precos)
novosPrecos = map(aumentarPreco, precos)
print("Preços novos:", list(novosPrecos))

print("--------------------")

def somarValor(valor):
    total = 0
    for v in valor:
        total += v
    return total

values = (1, 2) , [1, 2, 3] , (10, 20, 30, 40)
print(list(map(somarValor, values) ) )