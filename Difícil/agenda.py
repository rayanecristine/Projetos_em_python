# listas para armazenar contatos
nomes = []
telefones = []

opcao = 0  # inicializa a variável antes do while

# repetição
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
while opcao != 7:
    opcao = int(
        input(
            "Opções: \n"
            "1- LISTAR CONTATOS \n"
            "2- INSERIR CONTATO \n"
            "3- ALTERAR CONTATO \n"
            "4- BUSCAR CONTATO \n"
            "5- REMOVER CONTATO \n"
            "6- SALVAR EM ARQUIVO \n"
            "7- SAIR \n"
            "Sua opção: "
        )
    )  # responsável por receber opção digitada

    if opcao == 1:
        if nomes:
            for n in range(len(nomes)):
                print(nomes[n], "-----", telefones[n])
        else:
            print("Nenhum contato cadastrado.")
    
    elif opcao == 2:
        name = input("Nome: ")
        num = input("Número: ")
        nomes.append(name)
        telefones.append(num)
        print("Contato inserido com sucesso!")

    elif opcao == 3:
        alterar_contato = input("Qual contato você deseja alterar? ")
        if alterar_contato in nomes:
            i = nomes.index(alterar_contato)
            nomes[i] = input("Digite um novo nome: ")
            telefones[i] = input("Digite um novo número: ")
            print("Contato alterado com sucesso!")
        else:
            print("Contato não encontrado.")

    elif opcao == 4:
        buscar_contato = input("Qual contato você deseja buscar? ")
        if buscar_contato in nomes:
            i = nomes.index(buscar_contato)
            print("Contato encontrado:", nomes[i], "----", telefones[i])
        else:
            print("CONTATO NÃO ENCONTRADO!")

    elif opcao == 5:
        remover_contato = input("Qual contato você deseja remover? ")
        if remover_contato in nomes:
            i = nomes.index(remover_contato)
            del nomes[i]
            del telefones[i]
            print("CONTATO REMOVIDO!")
        else:
            print("Contato não encontrado.")

    elif opcao == 6:
        with open("contato.txt", "w") as arquivo:
            for s in range(len(nomes)):
                arquivo.write(nomes[s] + "-----" + str(telefones[s]) + "\n")
        print("CONTATOS SALVOS EM ARQUIVO.")

    elif opcao == 7:
        print("SAIR")
        break

    else:
        print("Opção inválida! Tente novamente.")
        
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")