proteinas = {
    "carne": {"ppg": 0.30},
    "peixe": {"ppg": 0.22},
    "ovo": {"ppu": 13},
    "laticinio": {"ppg": 0.032},
    "grãos": {"ppg": 0.10},
    "legume": {"ppg": 0.06},
    "fruta": {"ppg": 0.01}
}

relatorio = []
proteina_total = 0

def entrada_float_positiva(pergunta):
    while True:
        entrada = input(pergunta).replace(",", ".").strip()
        try:
            valor = float(entrada)
            if valor >= 0:
                return valor
            else:
                print("Dado inválido. Digite um número positivo.")
        except ValueError:
            print("Dado inválido. Digite um número.")

def entrada_int_positiva(pergunta):
    while True:
        entrada = input(pergunta).strip()
        try:
            valor = int(entrada)
            if valor >= 0:
                return valor
            else:
                print("Dado inválido. Digite um número inteiro positivo.")
        except ValueError:
            print("Dado inválido. Digite um número inteiro.")

for alimento in ["carne", "peixe", "laticinio", "grãos", "legume", "fruta"]:
    peso = entrada_float_positiva(f"Quantos gramas de {alimento} foram consumidos? ")
    proteina_total += proteinas[alimento]["ppg"] * peso

qtd_ovos = entrada_int_positiva("Quantos ovos foram consumidos? ")
proteina_total += proteinas["ovo"]["ppu"] * qtd_ovos

print(f"\nTotal de proteínas ingeridas: {proteina_total:.2f}g")

relatorio.append(f"\nTOTAL DE PROTEÍNAS: {proteina_total:.2f}g")

arquivo = open("proteinas_diarias.txt", "w", encoding="utf-8")
arquivo.write("proteinas diarias\n")
for linha in relatorio:
    arquivo.write(linha + "\n")
arquivo.close()

print("\nRelatório salvo como 'proteinas_diarias.txt'.")