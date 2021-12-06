print("Vamos calcular a média de suas refeições?")
mais1 = str(input("Deseja registrar uma refeição? S-sim/N-não: "))
refeicao = ""
refeicao_contador = 0
calorias = 0
total_calorias = 0

while mais1.upper() != "N":
    refeicao = str(input("Digite o que você comeu: "))
    refeicao_contador = refeicao_contador + 1
    calorias = int(input("Quantas calorias tinha sua refeição? "))
    total_calorias = total_calorias + calorias
    print(f"Você comeu {refeicao} para a sua {refeicao_contador}a refeição do dia. Essa refeição tem {calorias} calorias")
    mais1 = str(input("Deseja registrar uma refeição? S-sim/N-não: "))

media_calorias = total_calorias/refeicao_contador
print(f"A média de calorias por refeição do seu dia é de {media_calorias}.")