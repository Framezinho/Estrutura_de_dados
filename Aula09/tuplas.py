carros =  "Uno", "Gol", "Celta", "Palio", "Onix"
print(carros[-1]) # Onix
print(carros[-3:-1]) # Celta, Palio
print(carros[3:1:-1])  # Palio, Celta

def calcular(x, y):
    return x + y, x - y, x * y, x / y

resultado = calcular(10, 5)
print(resultado) 
for x in resultado:
    print("Resultado:", x)

a, b, c, d = calcular(10, 5)
print("Soma:", a)
print("Subtração:", b)
print("Multiplicação:", c)
print("Divisão:", d)