print("CALCULADORA")
valor1 = float(input("Digite o primeiro valor "))
valor2 = float(input("Digite o segundo valor "))
operacao = str(input("Qual operação quer fazer? +  -  /  * "))
resultado = 0
conta_executada = True
if operacao == "+":
    resultado = int(valor1) + int(valor2)
elif operacao == "-":
    resultado = int(valor1) - int(valor2)
elif operacao == "/":
    if valor2 ==0:
        conta_executada = False
        print("Não foi possivel realizar essa operação...")
    else:
        resultado = int(valor1) / int(valor2)
elif operacao == "*":
    resultado = int(valor1) * int(valor2)
else:
    conta_executada = False
    print("ERRO!")

if conta_executada == True:
    print(f"{resultado}")



