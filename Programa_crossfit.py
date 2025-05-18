import random

while True:
    print("\n=== MENU CROSSFIT ===")
    print("1 - Registrar treino do dia")
    print("2 - Calcular proteínas ingeridas")
    print("3 - Manipular treinos (adicionar, substituir, visualizar, remover)")
    print("4 - Treino aleatório")
    print("5 - Filtrar movimentos/treinos")
    print("6 - Gerenciar metas de desempenho")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # treinododia.py
        file = open("dia_a_dia.txt", "a", encoding='utf-8')
        exercicio = []
        lista = []
        dia = int(input("Que dia do mês é hoje? "))
        if dia < 0 or dia > 31:
            quit()
        else:
            ri = str(dia)
        mes = int(input("Em que mês estamos? "))
        if mes < 1 or mes > 12:
            quit()
        else:
            yue = str(mes)
        ano = int(input("Em que ano estamos? "))
        nian = str(ano)
        quantidade = int(input("Quantos exercícios foram realizados hoje? "))
        if quantidade < 1:
            print("resposta inválida")
            quit()
        for i in range(quantidade):
            exercício = input("Exercício feito hoje: ")
            exercicio.append(exercício)
            duração = float(input("Duração desse exercício em minutos: "))
            lista.append(str(duração))
        for i in range(len(exercicio)):
            a = exercicio[i]
            b = lista[i]
            file.write(ri + "/" + yue + "/" + nian + ' Exercício: ' + str(a) + ' Duração: ' + str(b) + '\n')
        file.close()

    elif opcao == "2":
        # proteinas_ingeridas.py
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
        arquivo.write("proteínas diárias\n")
        for linha in relatorio:
            arquivo.write(linha + "\n")
        arquivo.close()
        print("\nRelatório salvo como 'proteinas_diarias.txt'.")

    elif opcao == "3":
        # manipulaçãoDoTreino.py
        try:
            while True:
                escolha1 = input("Qual será a ação? (visualizar, adicionar, substituir, remover) ").lower()
                if escolha1 == 'adicionar':
                    file = open("Treino.txt", 'a')
                    quant = int(input("Quantos treinos você quer adicionar? "))
                    for i in range(quant):
                        adicionar = input("Insira o treino que você deseja adicionar: ")
                        tipagem = input("Insira o tipo de treino: ")
                        file.write(adicionar + ' tipagem: ' + tipagem + '\n')
                    file.close()
                elif escolha1 == 'substituir':
                    file = open("Treino.txt", 'r')
                    lista = file.readlines()
                    file.close()
                    for i in range(len(lista)):
                        print(f"Índice: [{i}] item: {lista[i]}")
                    sub = int(input("Qual o índice do item será substituído? "))
                    novo = input("Qual será o novo treino? ")
                    tipagem = input("Insira a sua tipagem: ")
                    lista[sub] = novo + ' tipagem: ' + tipagem + '\n'
                    file = open("Treino.txt", "w")
                    file.writelines(lista)
                    file.close()
                elif escolha1 == 'visualizar':
                    file = open("Treino.txt", 'r')
                    print(file.read())
                    file.close()
                elif escolha1 == 'remover':
                    file = open("Treino.txt", 'r')
                    lista = file.readlines()
                    file.close()
                    for i in range(len(lista)):
                        print(f"Índice: {i} item: {lista[i]}")
                    sub = int(input("Qual o índice do item será removido? "))
                    lista.pop(sub)
                    file = open("Treino.txt", "w")
                    file.writelines(lista)
                    file.close()
                else:
                    break
        except:
            breakpoint

    elif opcao == "4":
        # Aleatorio.py
        try:
            arquivo_treinos = open("dia_a_dia.txt", "r", encoding="utf8")
            lista_treinos = arquivo_treinos.readlines()
            arquivo_treinos.close()
            ultimo_treino = "50 Push-ups"
            while True:
                treino_aleatorio = random.choice(lista_treinos).strip()
                if treino_aleatorio != ultimo_treino:
                    print(f"\nQue tal o próximo treino ser {treino_aleatorio}?\n")
                    break
        except FileNotFoundError:
            print("\nErro: o arquivo dia_a_dia.txt não existe\n")

    elif opcao == "5":
        # Filtragem.py
        def filtrar(movtreino):
            existe_no_crud = 0
            try:
                crud = open("arquivo crud.txt", "r", encoding='utf8')
                linhascrud = crud.readlines()
                crud.close()
                filtrando = open("Filtro.txt", "w", encoding='utf8')
                for linha in linhascrud:
                    if movtreino in linha:
                        filtrando.write(linha + "\n")
                        existe_no_crud += 1
                filtrando.close()
                if existe_no_crud == 0:
                    print("Treino ou movimento não existe no crud.")
                else:
                    print("Filtragem concluída")
            except FileNotFoundError:
                print("Arquivo 'arquivo crud.txt' não encontrado.")
        Wodmov_filt = input("Insira o treino ou movimento que deseja filtrar: ").upper()
        filtrar(Wodmov_filt)

    elif opcao == "6":
        # Metas_de_desempenho.py
        def registrar_metas(meta):
            arquivo_metas = open("metas_de_desempenho.txt", "a", encoding="utf8")
            arquivo_metas.write(meta + "\n")
            arquivo_metas.close()
            print("Meta registrada")

        def acompanhar_metas(treino):
            try:
                arquivo_metas = open("metas_de_desempenho.txt", "r", encoding="utf8")
                lista_metas = arquivo_metas.readlines()
                for i in range(len(lista_metas)):
                    if str(treino) == lista_metas[i].strip("\n"):
                        del lista_metas[i]
                        arquivo_metas.close()
                        arquivo_metas = open("metas_de_desempenho.txt", "w", encoding="utf8")
                        arquivo_metas.writelines(lista_metas)
                        arquivo_metas.close()
                        print("Meta Alcançada!")
                        return
            except FileNotFoundError:
                print("\nErro: o arquivo metas_de_desempenho.txt não existe\n")

        try:
            quant_metas = int(input("Quantas metas deseja registrar? "))
            for i in range(quant_metas):
                meta = input("Digite a meta que deseja registrar: ").capitalize()
                registrar_metas(meta)
        except ValueError:
            print("Erro: é preciso digitar um valor inteiro")

        while True:
            treino_que_fiz = input("Fizesse o que hoje? ").capitalize()
            if treino_que_fiz == "Nada":
                break
            acompanhar_metas(treino_que_fiz)

    elif opcao == "0":
        print("Fechando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
