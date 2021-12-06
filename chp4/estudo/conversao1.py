escolha = int(input("Opção 1 para converter de Celsius para Fahrenheit ou 2 de Fahrenheit para Celsius: "))

if escolha == 1:
    inicio1 = float(input("Digite os graus em celsius: "))
    resultado = (inicio1 * 9/5) + 32
    print(f"A conversão foi feita: {resultado:.1f} graus fahrenheit")
elif escolha == 2:
    inicio2 = float(input("Digite os graus em Fahrenheit: "))
    resultado = 5 * (inicio2- 32) / 9
    print(f"A conversão foi feita: {resultado:.1f} graus Celsius")