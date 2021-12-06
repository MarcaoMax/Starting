print("Calculo de preço com desconto")

def cal(a,b):

    if b==1:
        c=a-(a*0.1)
    elif b==2:
        c=a-(a*0.05)
    elif b==3:
        c=a
    elif b==4:
        c=a+(a*0.07)
    return c

a=float(input("Digite o preço do produto: "))
b=int(input("Digite o método de pagamento. 1-A vista dinheiro | 2-A vista cartão de crédito | 3- Em 2 vezes | 4-Em 4 vezes "))

print(f"O preço original do produto é R$:{a}.")
print(f"O método de pagamento escolhido é o {b}.")
print(f"o preço a ser pago é R${cal(a,b)}.")