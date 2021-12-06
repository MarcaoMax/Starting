n=int(input("numero de partida: "))
for i in range (1,n+1):
    print(i)

#colocar na lista
lista=[]
for i in range (1,n+1):
    lista.append(i)

print(lista)

#outro programa
#soma numeros até digitar o 0
n=1
soma=0
while n!=0:
    n=int(input("Digite um numero: "))
    soma=soma+n

print(f"A soma total dos números é {soma}")