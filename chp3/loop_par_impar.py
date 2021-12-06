print("Calculo de médias dos alunos com numero par e impar")
total_impar=0
total_par=0
print("A seguir coloque a nota dos alunos de número impar:")
for a in range (1,51,2):
    print("Você está digitando a nota dos alunos impares")
    nota_impar = float(input(f"Digite a nota do aluno de número {a}: "))
    total_impar = nota_impar + total_impar
print("A seguir coloque a nota dos alunos de número par:")
for b in range (2,51,2):
    print("Você está digitando a nota dos alunos pares")
    nota_par = float(input(f"Digite a nota do aluno de número {b}: "))
    total_par = nota_par + total_par
print("Resultados:")
media_impar = total_impar/25
media_par = total_par/25

print(f"A média dos alunos de número impar é {media_impar}.")
print(f"A média dos alunos de número par é {media_par}.")

if media_impar>media_par:
    print("A média dos alunos de número impar é maior.")
elif media_par>media_impar:
    print("A média dos alunos de número par é maior.")
elif media_impar==media_par:
    print("As médias são iguais.")