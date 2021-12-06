print("Vamos escrever seu nome e idade?")

nome = input("Escrevea seu primeiro nome ")
sobrenome = input("Escreva seu sobrenome ")
ano_nasc = int(input("Digite o ano que você nasceu "))
idade = 2021 - ano_nasc

print(f"Olá! {nome} {sobrenome}! Bem vindo!")
print(f"Você tem {idade} anos!")