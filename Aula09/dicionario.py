carro01 = {"marca": "Fiat", "modelo": "Uno", "ano": 2020}
carro02 = {"marca": "Chevrolet", "modelo": "Onix", "ano": 2021}
carro03 = {"marca": "Volkswagen", "modelo": "Gol", "ano": 2019}
carro03["cor"] = "Prata"

print(carro01)
print(carro02["ano"])
carro03["ano"] = 2022
del carro02["modelo"]
print(carro03)