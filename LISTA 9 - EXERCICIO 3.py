hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
n = (input("Digite um número inteiro: "))
numeros = n.split()
n1 = int(numeros[0])
n2 = int(numeros[1])
n3 = int(numeros[2])

r = []
while n1 > 0:
    r.append(hex[(n1 % 16)])
    n1 = n1 // 16
    
    
if len(r) >= 2:
    j = r[0]
    r[0] = r[1]
    r[1] = j


    
    


while n2 > 0:
    r.append(hex[(n2 % 16)])
    n2 = n2 // 16


if len(r) > 3:
    j = r[2]
    r[2] = r[3]
    r[3] = j

    
        

while n3 >= 0:
    r.append(hex[(n3 % 16)])
    n3 = n3 // 16

if len(r) == 6:   
    j = r[4]
    r[4] = r[5]
    r[5] = j
elif len(r) == 5:
    j = r[3]
    r[3] = r[4]
    r[4] = j 

print('A cor {} em hex é: #' .format(numeros), end='')
for i in range(0, len(r)):
    print(r[i],end="")