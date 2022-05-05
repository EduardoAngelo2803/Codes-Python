qtdade = int(input())
presente = dict()


for i in range(qtdade):
    
    nome = input().split()
    presente[nome[0]] = nome[1], nome[2], nome[3]

conferencia = input().split()

while True:

    if conferencia[0] in presente:
        if conferencia[1] in presente[conferencia[0]]:
            print("Uhul! Seu amigo secreto vai adorar")

        else:
            print("Tente Novamente!")

    if "FIM" in conferencia:
        break

    conferencia = input().split()

 
 