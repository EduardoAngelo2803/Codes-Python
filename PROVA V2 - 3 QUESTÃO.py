new_dict = {}
def registerBooks(name_book, names_author, classification):
    global new_dict
    new_dict['Classificação'] = classification
    new_dict['Nome_Livro'] = name_book
    new_dict['names_author'] = names_author 

    return new_dict

nome_livro = input("Digite o nome do livro: ")
lista_nomeautor = []
nome_autor = input("Digite o nome do autor: ")
lista_nomeautor.append(nome_autor)
class_livro = input("Digite a classificação do livro: ")

registerBooks(nome_livro, nome_autor, class_livro)
for k, v in new_dict.items():
    print(new_dict)

acervo = {

    'sociologia': {

        'Pequeno manual antirracista': {

            'names_author': ['Djamila Ribeiro']

},  'Mulheres que correm com os lobos': {

            'names_author': ['Clarrisca Pinkola Estés']

},  '1984': {
            'names_author': ['George Orwell']

 },
},
    'auto ajuda': {
        'O poder do hábito': {

            'names_author': ['Charles Duhigg']

},
    'O milagre da manhã: O segredo para transformar sua vida (antes das 8 horas)': {

            'names_author': ['Hal Elrod']

 }
},
    'financeiro': {
        'Do mil ao Milhão. Sem cortar o cafezinho':{

            'names_author': ['Thiago Nigro']

},
    'Os segredos da mente milionária': {

            'names_author': ['T,Harv Eker']
 }
},
    'Tecnologia e Negócios': {

        'Transformação digital uma jornada possível': {
            
            'names_author': ['Eduardo Peixoto', 'César França', 'Eduardo Magrani', 'Fabio Maia', 'João Paulo', 'etc']

 },
}
}