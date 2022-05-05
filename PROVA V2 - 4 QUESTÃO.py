#função que recebe como parâmetro o name_book, 'inputado' pelo usuário.
def searchBooks(name):
    #Varrendo a lista acerto_total, que armazena o dicionário acervo dentro dela
    for m in acervo_total:
        #Se a variável 'm' estiver no dicionário acervo, na chave 'nome_livro', e se esse dado for igual ao name_book 'inputado' pelo usuário...
        if m['Nome_Livro'] in name:
            #Se confirmar o condicional acima, ele entra nesse laço para varrer os items do dicionário m, e pegar sua key e value.
            for k, v in m.items():
                print(f"{k} = {v}")

acervo = {}
acervo_total = []

acervo['Classificação'] = 'Sociologia'
acervo['Nome_Livro'] = 'Pequeno manual antirracista'
acervo['names_author'] = 'Djamila Ribeiro'
acervo_total.append(acervo.copy())
acervo.clear()
acervo['Classificação'] = 'Sociologia'
acervo['Nome_Livro'] = 'Mulheres que correm com os lobos'
acervo['names_author'] = 'Clarissa pinkola Estés'
acervo_total.append(acervo.copy())
acervo.clear()
acervo['Classificação'] = 'Sociologia'
acervo['Nome_Livro'] = '1984'
acervo['names_author'] = 'George Orwell'
acervo_total.append(acervo.copy())
acervo.clear()
acervo['Classificação'] = 'Auto Ajuda'
acervo['Nome_Livro'] = 'O poder do hábito'
acervo['names_author'] = 'Charles Duhigg'
acervo_total.append(acervo.copy())
acervo.clear()
acervo['Classificação'] = 'Auto Ajuda'
acervo['Nome_Livro'] = 'O milagre do amanhã: O segredo para transformar a vida(antes das 8 horas)'
acervo['names_author'] = 'Hal Elrod'
acervo_total.append(acervo.copy())
acervo.clear()
acervo['Classificação'] = 'Financeiro'
acervo['Nome_Livro'] = 'Do mil ao milhão. Sem cortar o cafezinho'
acervo['names_author'] = 'Thiago Nigro'
acervo_total.append(acervo.copy())
acervo.clear()
acervo['Classificação'] = 'Financeiro'
acervo['Nome_Livro'] = 'Os segredos da mente milionária'
acervo['names_author'] = 'T. Harv Eker'
acervo_total.append(acervo.copy())
acervo.clear()
acervo['Classificação'] = 'Tecnologia e Negócios'
acervo['Nome_Livro'] = 'Transformação Digital uma jornada possível'
acervo['names_author'] = 'Eduardo Peixoto, César França, Eduardo Mangrani, Fabio Maia, João Paulo, etc'
acervo_total.append(acervo.copy())
acervo.clear()


name_book = input("Digite o nome do livro que deseja procurar: ")
#Chamada da função searchBooks, passando como parâmetro 'name_book', que foi 'inputado' pelo usuário.
searchBooks(name_book)















