def pulaLinha():
    print('*/' * 30)

texto_c = ''
texto_novo_guard = []
list_pergunta = []
opc_salvar = []
opc_abrir = []
arquivo_o = ''

pulaLinha()
print(" BEM-VINDO AO EDITOR DE TEXTO!!"  *2)
pulaLinha()

texto_inic = input("Digite um texto: ")
texto_novo_guard.append(texto_inic)

while True:

    pergunta = input("O que você deseja fazer com o texto? \n c - escrever // r - ler // u - modificar // d - deletar // s - salvar // o - abrir // e - sair: ").lower()[0]
    list_pergunta.append(pergunta)
    if pergunta == 'c':
        texto_c = input("Digite mais textos: ")
        print()
        #Adicionando o o novo texto escrito na lista texto_novo_guard
        texto_novo_guard.append(texto_c[:])
    
    if pergunta == 'r':
        #Caso tenha sido escrito algo em Texto_c, ele printa a lista texto_novo guard.
        if len(texto_c) > 0:
            for l in texto_novo_guard:
                print(l, end=" ")
            print()
            print()
            

        else:
            #Caso não tenha sido escrito nada, ele apenas lê o texto_inic. Nesse caso, o texto_inic foi apendando na lista texto_novo_guard
            if len(list_pergunta) > 1:
                for l in texto_novo_guard:
                    print(l, end=" ")
                print()
                print()
            else:
                for l in texto_novo_guard:
                    print(l, end=" ")
                print()
                print()
            #Caso o usuário tenha decidido apagar tudo, ele mostra que o texto esta vazio até o momento!
            if len(texto_novo_guard) == 0:
                print("Seu texto esta vazio! Digite a opção 'C' no menu, para poder escrever algo nele!") 
                print()
    if pergunta == 'u':
        if len(texto_c) > 0:
            index = int(input(f"Diga qual o número da frase do texto: {texto_novo_guard}que irá ser modificada, a 1ª frase vale 0: "))
            index_u = str(input(f"Digite 2 palavras, separadas por 'espaço'. 1º A que será 'buscada' e 2º a que irá substitui-la no texto: {texto_novo_guard[index]}: ")).split()
            #Laço para passar por todas as palavras do texto
            for i in texto_novo_guard:
                if index_u[0] in i or index_u[1] in i:
                    #Armazenando o index da frase que será expluído e o que irá substituir numa variável 
                    texto_u = str(texto_novo_guard[index])
                    #Excluindo a palavra 'inputada' pelo usuário, no index determinado
                    texto_novo_guard.pop(index)
                    #Variável para armazenar o novo texto, com o 'replace' da palavra antiga, pela nova.
                    a = texto_u.replace(index_u[0], index_u[1])
                    texto_novo_guard.append(a)
                    print()
        #Caso não tenha sido escrito nada ainda além do texto inicial, entra nesse 'else', com as mesmas características do 'if' acima
        else:
            index = int(input(f"Diga qual o número da frase do texto: {texto_novo_guard}que irá ser modificada, a 1ª frase vale 0: "))
            index_u = str(input(f"Digite 2 palavras, separadas por 'espaço'. A que será 'buscada' e a que irá substitui-la na texto: {texto_novo_guard[index]}: ")).split()
            for l in texto_novo_guard:
                if index_u[0] in l:
                    texto_u = str(texto_novo_guard[0])
                    texto_novo_guard.pop(0)
                    a = texto_u.replace(index_u[0], index_u[1])
                    texto_novo_guard.append(a)
                    print()

    if pergunta == 'd':
        if len(texto_c) > 0:
            index_d = int(input(f"Diga o número da frase {texto_novo_guard}que deseja apagar, começando com 0: "))
            texto_novo_guard.pop(index_d)
            print()

        else:  
            index_d = int(input(f"Digite qual frase do texto: {texto_novo_guard} que deseja apagar, começando com 0: "))
            texto_novo_guard.pop(0)
            print("Seu texto ficou vazio!") 
            print()

    if pergunta == 's':
        opc_salvar.append(pergunta)
        texto_s = input("Digite o nome do arquivo que deseja salvar: ")
        #Caso o nome do arquivo que o usuário deseja salvar, for igual ao arquivo aberto, ele abre o mesmo arquivo.
        if texto_s == arquivo_o:
            file = open(arquivo_o, "a", encoding="utf-8")
        #Senão, ele abre o arquivo com o nome digitado pelo usuário.
        else:
            file = open(texto_s, "a", encoding="utf-8")
        if len(texto_novo_guard) > 0:
            #Laço que passa pelas palavras do texto , e escreve essas palavras no arquivo 
            for line in texto_novo_guard:
                file.write(line)
                file.write('\n')
        else:
            file.write(texto_inic)
            file.write('\n')
        file.close()

    if pergunta == 'o':
        arquivo_o = input("Qual nome do arquivo que deseja abrir? ")
        file = open(arquivo_o, 'a', encoding="utf-8")

    if pergunta == 'e':
        #Caso não tenha sido escolhida nenhuma opção no texto, irá ser apagado a ultima opção salva na lista, que no caso desse 'if', sempre será 'e'.
        if len(list_pergunta) > 1:
            list_pergunta.pop()
        #Essa condicional é para verificar se a ultima opção, além de salvar, foi para ler, que nesse caso, não modifica nada no texto :D
        if list_pergunta[len(list_pergunta) - 1] == 's' or list_pergunta[len(list_pergunta) -1] == 'r' and list_pergunta[len(list_pergunta) - 2] == 'r':
        
            #Aqui eu estou pegando apenas a primeira letra de sim ou não, e jogando para maiúsculo
                continuar = input("Deseja Sair? Sim/Não: ").upper()[0]

                if continuar == 'S':
                    break
        if list_pergunta[len(list_pergunta) - 1] == 'r':

            break
                
        else:#Aqui eu estou pegando apenas a primeira letra de sim ou não, e jogando para maiúsculo
            salvando = input("Você não salvou a ultima alteração do arquivo!! Deseja salvar antes de sair? Sim/Não: ").upper()[0]
            if salvando not in 'SN':
                print("Digite apenas Sim ou Não!")
                continue
            #Caso o usuário deseja salvar, ele pergunta o nome do arquivo, abre o arquivo, escreve nele, e fecha!
            if salvando == 'S':
                texto_s = input("Digite o nome do arquivo que deseja salvar: ")
                file = open(texto_s, "a", encoding="utf-8")
                if len(texto_novo_guard) > 0:
                    for line in texto_novo_guard:
                        file.write(line)
                        file.write('\n')
                else:
                    file.write(texto_inic)
                    file.write('\n')
                file.close()
                break
            if salvando == 'N':
                break
     
pulaLinha()
print("Fechando o Programa, até a próxima!!")