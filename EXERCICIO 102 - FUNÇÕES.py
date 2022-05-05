def fatorial(fat, show):
    
    j = 1
    for c in range(fat, 0, -1):
        j *= c
        if show == 1:
            
            print(f"{fat} X ", end='')
            fat -= 1
    if show == 1:
        print(f"= {j}", end='')
    if show == 0:
        print(j)

   

f = int(input("Digite o numero fatorial: "))
g = int(input("Show é True ou False? 0 - Para False // 1 - Para True: "))

fatorial(f, g)