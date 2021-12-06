from calc_func import*
#chamar função do módulo!

print("CALCULADORA")
print("")

valor1=float(input("Digite o primeiro valor: "))
valor2=float(input("Digite o segundo valor: "))

chamar=str(input("Digite a operação que deseja usar: + | - | * | / : "))

if chamar=="+":
    print(somar(valor1,valor2))
elif chamar=="-":
    print(subt(valor1,valor2))
elif chamar=="*":
    print(mult(valor1,valor2))
elif chamar=="/":
    print(divi(valor1,valor2))
else:
    print("Operação inválida, tente novamente.")

