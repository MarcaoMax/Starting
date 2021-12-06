print("Vamos votar para decidir qual console iremos ganhar?")
print("")

total_xbox = 0
total_play = 0
total_nintendo = 0

voto1 = int(input("Primeiro voto. Digite: 1 para XBOX, 2 para Playstation ou 3 para Nintendo! "))
print("")

if voto1 == 1:
    total_xbox = total_xbox + 1
elif voto1 == 2:
    total_play = total_play + 1
elif voto1 == 3:
    total_nintendo = total_nintendo + 1
else:
    print("Voto inválido")

voto2 = int(input("Segundo voto. Digite: 1 para XBOX, 2 para Playstation ou 3 para Nintendo!"))
print("")

if voto2 == 1:
    total_xbox = total_xbox + 1
elif voto2 == 2:
    total_play = total_play + 1
elif voto2 == 3:
    total_nintendo = total_nintendo + 1
else:
    print("Voto inválido")

voto3 = int(input("Terceiro voto. Digite: 1 para XBOX, 2 para Playstation ou 3 para Nintendo!"))
print("")

if voto3 == 1:
    total_xbox = total_xbox + 1
elif voto3 == 2:
    total_play = total_play + 1
elif voto3 == 3:
    total_nintendo = total_nintendo + 1
else:
    print("Voto inválido")

voto4 = int(input("Quarto voto. Digite: 1 para XBOX, 2 para Playstation ou 3 para Nintendo!"))
print("")

if voto4 == 1:
    total_xbox = total_xbox + 1
elif voto4 == 2:
    total_play = total_play + 1
elif voto4 == 3:
    total_nintendo = total_nintendo + 1
else:
    print("Voto inválido")

voto5 = int(input("Quinto voto. Digite: 1 para XBOX, 2 para Playstation ou 3 para Nintendo!"))
print("")

if voto5 == 1:
    total_xbox = total_xbox + 1
elif voto5 == 2:
    total_play = total_play + 1
elif voto5 == 3:
    total_nintendo = total_nintendo + 1
else:
    print("Voto inválido")

print("")
print("Resultado da votação:")
print("")
print(f"Votos para o XBOX: {total_xbox}")
print(f"Votos para o Playstation: {total_play}")
print(f"Votos para o Nintendo: {total_nintendo}")

if total_nintendo > total_xbox and total_nintendo > total_play:
    print("Vamos todos ganhar um Nintendo!")
elif total_xbox > total_nintendo and total_xbox > total_play:
    print("Vamos todos ganhar um XBOX!")
elif total_play > total_nintendo and total_play > total_xbox:
    print("Vamos todos ganhar um Playstation!")
else:
    print("Vamos ter que votar de novo...")