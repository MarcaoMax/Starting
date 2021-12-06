qtd = int(input("Qtd alunos:"))

soma = 0

for i in range(qtd):
    num = float(input("informe nota {}º aluno: ".format(i+1)))
    
    #solucao do problema 9
    while num < 0 or num > 10:
        print("Nota inválida, digite novamente")
        num = float(input("informe nota {}º aluno: ".format(i+1)))
    #fim da solucao do problema 9

    soma = soma + num

print(soma / qtd)    

