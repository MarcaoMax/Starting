nota=0
alunos=int(input("Digite o número de alunos: "))
soma=0

for i in range(1,alunos+1):
    nota=float(input(f"Informe a nota do aluno {i}: "))
    soma=nota+soma


media=soma/alunos

print(media)