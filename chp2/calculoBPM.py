print("Vamos avaliar seus BPM?")
print("")
idade = int(input("Digite sua idade: "))
bpm = int(input("Digite seu bpm: "))

if idade <= 2:
    if bpm > 140 and bpm < 250:
        print("Está alto demais!")
    elif bpm < 120:
        print("Está baixo demais!")
    elif bpm >= 120 and bpm <=140:
        print("Seus BPM estão no padrão certo!")
    elif bpm >= 250 or bpm < 1:
        print("Você está morto... meus pesâmes...")
elif idade > 2 and idade < 8:
    if bpm > 120 and bpm < 250:
        print("Está alto demais!")
    elif bpm < 100:
        print("Está baixo demais!")
    elif bpm <= 120 and bpm >=100:
        print("Seus BPM estão no padrão certo!")
    elif bpm >= 250 or bpm < 1:
        print("Você está morto... meus pesâmes...")
elif idade >=8 and idade <=17:
    if bpm > 100 and bpm < 250:
        print("Está alto demais!")
    elif bpm < 80:
        print("Está baixo demais!")
    elif bpm >=80 and bpm <=100:
        print("Seus BPM estão no padrão certo!")
    elif bpm >= 250 or bpm < 1:
        print("Você está morto... meus pesâmes...")
elif idade >=18 and idade <=65:
    if bpm > 80 and bpm < 250:
        print("Está alto demais!")
    elif bpm < 70:
        print("Está baixo demais!")
    elif bpm >= 70 and bpm <= 80:
        print("Seus BPM estão no padrão certo!")
    elif bpm >= 250 or bpm < 1:
        print("Você está morto... meus pesâmes...")
elif idade > 65:
    if bpm > 60 and bpm < 250:
        print("Está alto demais!")
    elif bpm < 50:
        print("Está baixo demais!")
    elif bpm >= 50 and bpm <=60:
        print("Seus BPM estão no padrão certo!")
    elif bpm >= 250 or bpm < 1:
        print("Você está morto... meus pesâmes...")