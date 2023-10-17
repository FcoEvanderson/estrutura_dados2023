import funcoes


def menu():
    print('''
    ============Editor de Lista=============
     |1-Exibir Lista     2-Inserir        |
     |3-Remover          4-Exibir Elemento|
     |5-Exibir Seleção   6-Evaziar        |
     |0-Sair                              |
    ========================================''')
    opcao = int(input("Sua opção ==> "))
    return opcao


def principal():
    lista = []
    while True:
        opcao = menu()
        if 0 <= opcao <= 6:
            if opcao != 0:
                if opcao == 1:
                    funcoes.mostrar(lista)
                elif opcao == 2:
                    funcoes.inserir(lista)
                elif opcao == 3:
                    pass
                elif opcao == 4:
                    if not lista.estaVazia():
                        pos = int(input("Digite a posição: "))
                        if 0 <= pos < lista.n:
                            lista.remover(pos)
                elif opcao == 5:
                    pass
                elif opcao == 6:
                    if not lista.estaVazia:
                        pos = int(input("Digite a posição: "))
                        i = lista.pesquisar_pos(pos)
                        if i >= 0:
                            print(f"Valor: {lista.get(i)}")
                    else:
                        print("A lista esta vazia!")
            else:
                break
        else:
            print("Valor inválido!")


if __name__ == "__main__":
    principal()