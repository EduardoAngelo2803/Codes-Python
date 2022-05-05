music = input().replace("a", "@").replace("E", "%").replace("e", "!").replace("i", "@").replace("o", "#").replace("u", "$").replace(" ", "").title()
num_senhas = int(input())
num_user = int(input())
ll = True

while ll == True:
    if num_user < 6:
        num_user = int(input())
    else:
        ll = False

for i in range(num_senhas): 
    senha_gerada = (f"{music[i:5+1]}{music[-5:]}{music[num_user:num_user+5]}") 
    new_senha = senha_gerada[::-1]

    print(new_senha)

resp_s_n = input()

while True:
    if resp_s_n == 'n':
        senha_gerada = (f"{music[i:5+1]}{music[-5:]}{music[num_user:num_user+5]}") 
        new_senha = senha_gerada[::-1]

        print(new_senha)
    

printando_user_senha = dict()


printando_user_senha[nome_usuario] = senha_gerada[::-1]

print(printando_user_senha)



