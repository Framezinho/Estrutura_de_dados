import json

texto = "João da Silva - Rua A, 132; Maria dos Santos - Rua B, 225"

def texto_para_lista(texto):
   
    pessoas = []

    registros = [r.strip() for r in texto.split(";") if r.strip()]
    for reg in registros:
      
        if "-" not in reg:
            continue
        nome_part, endereco_part = reg.split("-", 1)
        nome = nome_part.strip()

        if "," in endereco_part:
            endereco, numero = endereco_part.split(",", 1)
            endereco = endereco.strip()
            numero = numero.strip()
        else:
            endereco = endereco_part.strip()
            numero = ""
        pessoas.append({"nome": nome, "endereco": endereco, "numero": numero})
    return pessoas


def texto_para_json(texto, *, indent=4):
    lista = texto_para_lista(texto)
    return json.dumps(lista, ensure_ascii=False, indent=indent)


def main():
    j = texto_para_json(texto)
    print(j)


if __name__ == "__main__":
    main()
