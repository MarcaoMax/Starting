#Problema 7 e 8
import random

sorteado = random.randint(1, 1000)
chute = int(input("informe seu chute: "))
tentativas = 1

while chute != sorteado and tentativas <= 10:    
    if sorteado < chute:
        print("Tente um nº menor")    
    elif sorteado > chute:
        print("Tente um nº maior")
    chute = int(input("informe seu chute: "))
    tentativas = tentativas + 1

if chute == sorteado:
    print("Parabéns, você acertou!")
    print("Você fez {} tentativas".format(tentativas))
else:
    print("Você não acertou, o numero era {}".format(sorteado))    
