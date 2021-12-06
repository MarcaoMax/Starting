nota = float(input("nota: "))

while nota < 0 or nota > 10:
    print("Nota inválida, digite novamente")
    nota = float(input("nota: "))

print(nota)   