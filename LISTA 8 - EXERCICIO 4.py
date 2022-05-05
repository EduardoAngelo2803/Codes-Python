valores = {'1': 2.50, '2': 4.75, '3': 3.25, '4': 2.80, '5': 0.9}
quant = 1


item = 1

while item != 0:
    
    
    item = int(input())
    quant = int(input())
    
    if item > 5 or item < 1:
        print("Digite um código válido!")
    if item == 1:
        print(f"Você escolheu Cachorro quente")
    if item == 2:
        print("Você escolheu X-Tudo")
    if item == 3:
        print("Você escolheu Batata frita")
    if item == 4:
        print("Você escolheu Refrigerante")
    if item == 5:
        print("Você escolheu Pipoca")
    if item != 0:
        print(f"Sua conta é de R$ {item*quant}")

