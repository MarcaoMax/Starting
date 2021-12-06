#passwords

arquivo = open("passwords.txt", "r")

passwords = arquivo.readlines()

senhas=[]
arquivo.close()

lugar=input("Digite da onde é a senha: ")
usuario=input("Digite o nome de usuário: ")
senha=input("Digite a senha: ")

senhas.append([lugar+":"+"\n",[usuario+"\n",senha+"\n"]])

x=0

for x in range(0,len(passwords)-1,4):
    f=passwords[x]
    g=passwords[x+1]
    h=passwords[x+2]
    senhas.append([f,[g,h]])


senhas.sort()

arquivo = open("passwords.txt", "w")
for element in senhas:
    for i in range(0,1):
        arquivo.write(f"{element[0]}")
        for a in range(1):
            a=0
            arquivo.write(f"{element[1][a]}{element[1][a+1]}")
    arquivo.write("\n")
arquivo.close()