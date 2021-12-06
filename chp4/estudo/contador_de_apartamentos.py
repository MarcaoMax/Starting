def numeracao(a,b): #a = total de andares b =total de apts por andar
    for i in range(1,a+1):
        a=i
        print(f"Apartamentos do andar {i}:")
        for x in range(1,b+1):
            b=x
            print(f"{a}{b}")
        
    return a, b

numeracao(10,4)