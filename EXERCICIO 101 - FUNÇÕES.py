def voto(a):
    a = 2021 - ano
    if a >= 18 and a < 65:
        print(f"Com {a} anos: VOTO OBRIGATÓRIO")
        
    elif a < 18:
        print(f"Com {a} anos: NÃO VOTA")
        

    elif a > 65:
        print(f"Com {a} anos: VOTO OPICIONAL")
        


ano = int(input("Em que ano você nasceu? "))

voto(ano)