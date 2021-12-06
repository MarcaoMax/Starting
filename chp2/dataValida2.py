print("Validar entrada de data: DIA e MÊS.")
dia=int(input("Digite o dia: "))
mes=int(input("Digite o mês: "))
ano=int(input("Digite o ano: "))


if dia>0 and dia<=31 and mes>0 and mes<=12 and ano>=0 and ano<=2021:
    if ano%4==0 or ano%400==0 and ano%100!=0:
        if mes==2 and dia>29:
            print("Esse ano é bissexto! Fevereiro tem apenas 29 dias!")
        else:
            print(f"A data {dia}/{mes}/{ano} é válida!")
    elif mes==4 and dia>30:
        print("Abril tem apenas 30 dias. Data inválida.")
    elif mes==6 and dia>30:
        print("Junho tem apenas 30 dias. Data inválida.")
    elif mes==9 and dia>30:
        print("Setembro tem apenas 30 dias. Data inválida.")
    elif mes==11 and dia>30:
        print("Novembro tem apenas 30 dias. Data inválida.")
    elif mes==2 and dia>28:
        print("Nesse ano fevereiro tem apenas 28 dias. Data inválida")
    else:
        print(f"A data {dia}/{mes}/{ano} é válida!")
else:
    print("Data inválida")


#outra opção!

print("Validar entrada de data: DIA e MÊS.")
dia=int(input("Digite o dia: "))
mes=int(input("Digite o mês: "))
ano=int(input("Digite o ano: "))


if dia>0 and dia<=31 and mes>0 and mes<=12 and ano>=0 and ano<=2021:
    if ano%4==0 or ano%400==0 and ano%100!=0:
        if mes==2 and dia>29:
            print("Esse ano é bissexto! Fevereiro tem apenas 29 dias!")
        else:
            print(f"A data {dia}/{mes}/{ano} é válida!")
    elif mes==4 or mes==6 or mes==9 or mes==11 and dia>30:
        print("Esse mês tem apenas 30 dias. Data inválida.")
    elif mes==2 and dia>28:
        print("Nesse ano fevereiro tem apenas 28 dias. Data inválida")
    else:
        print(f"A data {dia}/{mes}/{ano} é válida!")
else:
    print("Data inválida")