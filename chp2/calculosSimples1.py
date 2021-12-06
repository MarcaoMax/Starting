print("Calculo de velocidade média de um objeto!")
distancia = input("Qual a distância percorrida em metros? ")
tempo = input("Quantos minutos para percorrer a distância? ")
vel_media = float(distancia) / float(tempo)
#metodo para mostrar apenas 2 casas decimais!
print(f"A velociade média é de {vel_media:.2f} metros/minuto.")