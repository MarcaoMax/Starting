print("Qual o melhor dia para ter Live?")
print("Vamos votar?")
segunda = int(input("Quantos votos para que a live aconteça na segunda-feira? "))
terca = int(input("Quantos votos para que a live aconteça na terça-feira? "))
quarta = int(input("Quantos votos para que a live aconteça na quarta-feira? "))
quinta = int(input("Quantos votos para que a live aconteça na quinta-feira? "))
sexta = int(input("Quantos votos para que a live aconteça na sexta-feira? "))
print("Resultado:")

if segunda>terca and segunda>quarta and segunda>quinta and segunda>sexta:
    print("Segunda-feira é o melhor dia para a maioria")
elif segunda==terca and segunda>quarta and segunda>quinta and segunda>sexta:
    print("Empate...Vamos ter que votar de novo...")
elif segunda>terca and segunda==quarta and segunda>quinta and segunda>sexta:
    print("Empate...Vamos ter que votar de novo...")
elif segunda>terca and segunda>quarta and segunda==quinta and segunda>sexta:
    print("Empate...Vamos ter que votar de novo...")
elif segunda>terca and segunda>quarta and segunda>quinta and segunda==sexta:
    print("Empate...Vamos ter que votar de novo...")
elif terca>quarta and terca>quinta and terca>sexta and terca>segunda:
    print("Terça-feira é o melhor dia para a maioria")
elif terca==quarta and terca>quinta and terca>sexta and terca>segunda:
    print("Empate...Vamos ter que votar de novo...")
elif terca>quarta and terca==quinta and terca>sexta and terca>segunda:
    print("Empate...Vamos ter que votar de novo...")
elif terca>quarta and terca>quinta and terca==sexta and terca>segunda:
    print("Empate...Vamos ter que votar de novo...")
elif quarta>quinta and quarta>sexta and quarta>segunda and quarta>terca:
    print("Quarta-feira é o melhor dia para a maioria")
elif quarta==quinta and quarta>sexta and quarta>segunda and quarta>terca:
    print("Empate...Vamos ter que votar de novo...")
elif quarta>quinta and quarta==sexta and quarta>segunda and quarta>terca:
    print("Empate...Vamos ter que votar de novo...")
elif quinta>sexta and quinta>segunda and quinta>terca and quinta>quarta:
    print("Quinta-feira é o melhor dia para a maioria")
elif quinta==sexta and quinta>segunda and quinta>terca and quinta>quarta:
    print("Empate...Vamos ter que votar de novo...")
elif sexta>segunda and sexta>terca and sexta>quarta and sexta>quinta:
    print("Sexta-feira é o melhor dia para a maioria")
print(f"Total de votos para segunda-feira: {segunda}")
print(f"Total de votos para terça-feira: {terca}")
print(f"Total de votos para quarta-feira: {quarta}")
print(f"Total de votos para quinta-feira: {quinta}")
print(f"Total de votos para sexta-feira: {sexta}")

