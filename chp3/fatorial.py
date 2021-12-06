print("Programa para calcular o fatorial de um número")
num = int(input("Digite o número dos minutos: "))
a = 1
  
for b in range(1,num+1):
    a = a*b
      
print (f"A senha é LIBERDADE{a}")

#segundo jeito

print("Programa para calcular o fatorial de um número")
num = int(input("Digite o número dos minutos: "))
a = 1
contador=1
  
while contador<=num:
    a=a*contador
    contador=contador+1

print (f"A senha é LIBERDADE{a}")