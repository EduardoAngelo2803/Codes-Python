temp = {}
temp2 = {}
contas2 = []
moradores_casa = []

try:
    qtdade_pessoas = int(input("Quantas pessoas tem na casa? "))
    #Laço que roda de acordo com a quantidade de pessoas na casa, pedindo seu nome e sua renda.
    for i in range(0, qtdade_pessoas):
        #Adiciona a pessoa e a renda, no dicionário Temp, de temporário, para depois adicioná-los em uma lista para guardar as informações.
        temp['pessoa'] = input(f"Digite o nome da {i+1}ª pessoa: ")
        temp['renda'] = input(f"Digite a renda da pessoa {temp['pessoa']}: ")
        temp['renda'] = int(temp['renda'])
        #Fazendo uma cópia do dicionário para lista, e logo em seguida apagando o dicionário, para registrar uma nova pessoa com sua renda.
        moradores_casa.append(temp.copy())
        temp.clear()
    qtdade_contas = int(input("Quantas contas tem para pagar? "))
    #Laço que roda de acordo com a quantidade de contas a serem pagas.
    for i in range(0, qtdade_contas):
        #Adiciona a conta e seu valor, no dicionário Temp2, de temporário, para depois adicioná-los em uma lista para guardar as informações.
        temp2['conta'] = input(f"Digite o nome da {i+1}ª conta: ")
        temp2['conta_valor'] = input(f"Digite o valor da conta {temp2['conta']}: ")
        temp2['conta_valor'] = int(temp2['conta_valor'])
        #Fazendo uma cópia do dicionário para lista, e logo em seguida apagando o dicionário, para registrar uma nova conta com seu valor.
        contas2.append(temp2.copy())
        temp2.clear()

    conta_total = 0
    #Laço para calcular o valor total das contas da casa
    for v in contas2:
        conta_total += v['conta_valor'] 
        conta_total = int(conta_total)

    renda_total = 0
    #Laço para calcular o valor total da renda dos moradores da casa
    for i in moradores_casa:
        renda_total += i['renda']
        renda_total = int(renda_total)
    #Caso a soma das contas seja maior que a soma das rendas, ele printa essa informação na tela.
    if conta_total > renda_total:
        divida = conta_total - renda_total
        print(f"A família precisa fazer corte nos gastos! pois esse Mês vai ficar faltando R${divida} para quitar todas as contas!")
    #Senão, ele entra em um laço para calcular quanto cada morador deve pagar, de acordo com a fórmula matemática da variável dist_valor
    else:
        for c in moradores_casa:
            dist_valor = c['renda']/renda_total * conta_total
            print(f"A pessoa {c['pessoa']} deve pagar = R$ {dist_valor}")  
#Caso a renda da familia seja zerada, a variável dist_valor teria uma divisão por zero, que entra nesse except, para informar a mensagem abaixo.
except ZeroDivisionError as zde:
    print(F"A família não teve renda esse mês! ao todo, ficou uma dívida de {conta_total} a ser paga próximo mês!")

except ValueError as ve:
    print("Por favor, digite apenas números nessa opção!")
