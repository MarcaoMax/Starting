print("CALCULADORA")
print("")

def somar(a,b):
    res=a+b
    return res
def subt(a,b):
    res=a-b
    return res
def mult(a,b):
    res=a*b
    return res
def divi(a,b):
    if b==0:
        print("Números não podem ser divididos por 0!")
    else:
        res=a/b
        return res

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
