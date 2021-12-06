import math
num = float(input("numero "))
if num <0:
    print("numero nao exite")
else:
    raiz = math.sqrt(num)
    print(raiz)

time1 = int(input("time X "))
time2 = int(input("time Y "))
if time1 == time2:
    print("empate")
elif time1 > time2:
    print("time X venceu")
elif time2 > time1:
    print("time Y venceu")

salario = float(input("Digite salario: "))
valor=0
if salario<=1693.72:
    valor=0.08
elif salario<=2822.90:
    valor=0.09
elif salario<=5645.80:
    valor=0.11
else:
    porcentagem=621.038

porcentagem=salario*valor
print(f"Valor a pagar {porcentagem}")