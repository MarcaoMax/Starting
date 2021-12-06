print("Validar entrada de data: DIA e MÊS.")
dia=int(input("Digite o dia: "))
mes=int(input("Digite o mês: "))

if dia>0 and dia<=31 and mes>0 and mes<=12:
    print(f"A data {dia}/{mes} é válida!")
else:
    print("A data é inválida")