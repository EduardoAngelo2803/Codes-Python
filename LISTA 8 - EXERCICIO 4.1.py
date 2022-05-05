item = ('Cachorro Quente', 'X-Tudo', 'Batata frita', 'Refrigerante', 'Pipoca')
valor = (2.50, 4.75, 3.25, 2.80, 0.90)
entrada = 1
resul = 0
    
while entrada != 0:

    entrada = int(input())
    if entrada == 0:
        print("Código inválido")
        break
    #elif entrada >=1 and entrada <= 5:
        #quant = int(input())
           
    if entrada == 1:
        print(f"Você escolheu {item[0]}")
        quant = int(input())
        print("Sua conta é de R${}" .format(valor[0]*quant))
    elif entrada == 2:
        print(f"Você escolheu {item[1]}")
        quant = int(input())
        print("Sua conta é de R${}" .format(valor[1]*quant))
    elif entrada == 3:
        print(f"Você escolheu {item[2]}")
        quant = int(input())
        print("Sua conta é de R${}" .format(valor[2]*quant))
    elif entrada == 4:
        print(f"Você escolheu {item[3]}")
        quant = int(input())
        print("Sua conta é de R$ {}" .format(valor[3]*quant))
    elif entrada == 5:
        print(f"Você escolheu {item[4]}")
        quant = int(input())
        print("Sua conta é de R${}" .format(valor[4]*quant))
    
   

