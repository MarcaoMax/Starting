print("Vamos calcular os custos da viagem e os descontos?")
print("")
valor_viagem = float(input("Digite o valor total da viagem: "))
passageiros = int(input("Digite o número de passageiros de 1 a 4: "))
classe = int(input("Digite o número referente a classe da viagem comprada: 3-Econômica, 2-Executiva ou 1-Primeira classe: "))

if classe == 3:
    if passageiros == 1:
        desconto = 1
        print("Não possuimos desconto para apenas um passageiro.")
    elif passageiros == 2:
        desconto = 0.03
        print("Desconto de 3%!")
    elif passageiros == 3:
        desconto = 0.04
        print("Desconto de 4%!")
    elif passageiros == 4:
        desconto = 0.05
        print("Desconto de 5%!")
elif classe == 2:
    if passageiros == 1:
        desconto = 1
        print("Não possuimos desconto para apenas um passageiro.")
    elif passageiros == 2:
        desconto = 0.05
        print("Desconto de 5%!")
    elif passageiros == 3:
        desconto = 0.07
        print("Desconto de 7%!")
    elif passageiros == 4:
        desconto = 0.08
        print("Desconto de 8%!")
elif classe == 1:
    if passageiros == 1:
        desconto = 1
        print("Não possuimos desconto para apenas um passageiro.")
    elif passageiros == 2:
        desconto = 0.1
        print("Desconto de 10%!")
    elif passageiros == 3:
        desconto = 0.15
        print("Desconto de 15%!")
    elif passageiros == 4:
        desconto = 0.2
        print("Desconto de 20%!")
else:
    print("Ocorreu um erro, começe novamente!")

valor_desconto = valor_viagem*desconto
valor_liq = valor_viagem - valor_desconto
valor_medio = valor_liq/passageiros

print("")
print("A seguir os dados das suas despesas para essa viagem:")
print("")
print(f"O valor a pagar sem desconto seria de: R${valor_viagem}")
print(f"Mas você ganhou um desconto de: R${valor_desconto}")
print(f"E vai acabar pagando apenas: R${valor_liq}")
print(f"Isso dá um total de R${valor_medio} por pessoa!")
