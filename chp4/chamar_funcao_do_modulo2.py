from calc_func import*

operacao=0
while operacao!=5:
    print("Para realizar uma operação de soma, digite 1.")
    print("Para realizar uma operação de subtração, digite 2.")
    print("Para realizar uma operação de multiplicação, digite 3.")
    print("Para realizar uma operaçãp de divisão, digite 4.")
    print("Para sair digite 5.")
    operacao=int(input(": "))
    
#prestar atenção nos parenteses no caso abaixo!
    if operacao==1:
        print(somar(float(input("Digite o primeiro valor: ")),float(input("Digite o segundo valor: "))))
    elif operacao==2:
        print(subt(float(input("Digite o primeiro valor: ")),float(input("Digite o segundo valor: "))))
    elif operacao==3:
        print(mult(float(input("Digite o primeiro valor: ")),float(input("Digite o segundo valor: "))))
    elif operacao==4:
        print(divi(float(input("Digite o primeiro valor: ")),float(input("Digite o segundo valor: "))))
    else:
        print("Até logo!")