print("Calculo de preço com desconto")
preco=float(input("Digite o preço do produto: "))
met=int(input("Digite o método de pagamento. 1-A vista dinheiro | 2-A vista cartão de crédito | 3- Em 2 vezes | 4-Em 4 vezes "))

pago=0

if met==1:
    pago=preco-(preco*0.1)
elif met==2:
    pago=preco-(preco*0.05)
elif met==3:
    pago=preco
elif met==4:
    pago=preco+(preco*0.07)

print(f"O preço do produto é R$:{preco}.")
print(f"O método de pagamento escolhido é o {met}.")
print(f"o preço a ser pago é R${pago}.")