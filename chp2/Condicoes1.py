peso = float(input("Peso da bagagem: "))

if peso <= 28:
    print("tudo OK! Pode embarcar!")
else:
    plano = str(input("Você possui plano premium? S-sim / N-não: "))
    if plano == "n":
        print("Sua bagagem está acima do peso!")
    elif peso > 32:
        print("Sua bagagem está acima do peso!")
    else:
        print("tudo OK! Pode embarcar!")