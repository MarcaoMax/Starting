entrada=[37,212,0,-40,0]
i=0
for i in range(len(entrada)):
    if i == 0 or i == 2:
        resultado = (entrada[i] * 9/5) + 32
        print(f"{entrada[i]} graus Celsius para {resultado} graus Fahrenheit.")
    elif i == 1 or i == 3:
        resultado = 5 * (entrada[i]- 32) / 9
        print(f"{entrada[i]} graus Fahrenheit para {resultado} graus Celsius")
    elif i == 4:
        resultado = entrada[i]-273.15
        print(f"{entrada[i]} graus Kelvin para {resultado} graus Celsius")