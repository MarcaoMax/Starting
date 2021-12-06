print("colocar os números em ordem crescente!")
num1=int(input("Digite o 1o número: "))
num2=int(input("Digite o 2o número: "))
num3=int(input("Digite o 3o número: "))

if num1>=num2>=num3:
    print(num1,num2,num3)
elif num1>=num3>=num2:
    print(num1,num3,num2)
elif num2>=num1>=num3:
    print(num2,num1,num3)
elif num2>=num3>=num1:
    print(num2,num3,num1)
elif num3>=num1>=num2:
    print(num3,num1,num2)
elif num3>=num2>=num1:
    print(num3,num2,num1)