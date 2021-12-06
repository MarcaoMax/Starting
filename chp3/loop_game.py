import random

aleatorio=random.randint(1,1000)
guess=2000
tentativas=0
print("Acerte o número sorteado de 1 a 1000 em no máximo 10 tentativas!")
while guess!=aleatorio:
    tentativas=tentativas+1
    guess=int(input(f"Tente acertar o número tentativa {tentativas}: "))

    if tentativas==10:
        guess==aleatorio
        print("Você não acertou...")
        break
    elif aleatorio>guess:
        print("Tente um número maior")
    elif aleatorio<guess:
        print("Tente um número menor")
    elif aleatorio==guess:
        print(f"Acertou! Demorou {tentativas} tentativas!")
