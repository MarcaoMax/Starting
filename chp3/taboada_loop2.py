#taboada do 3
principal = 3
secundario = 1
resultado = 1

while resultado <= 30:
    print(resultado)
    resultado = principal*secundario
    secundario = secundario+1

print("final")

#aula
n = int(input("Qual numero voce quer a tabuada? "))
contador = 1

while contador <= 10:
    print(contador*n)
    contador = contador + 1