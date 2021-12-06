#usando a função open para criar um objeto do tipo arquivo
arquivo = open("i_can_see.txt")

#printando uma linha do arquivo
print(arquivo.readline())

#printando outra linha do arquivo
print(arquivo.readline())

#Exibindo uma linha por vez, utilizando o loop for e o método readlines()
for linha in arquivo.readlines():
    print(linha)


#Passando o conteúdo do arquivo para uma lista
linhas_do_arquivo = arquivo.readlines()

#comprovando o tipo do objeto linhas_do_arquivo
print("Ei! Eu consegui transformar meu arquivo em uma {} ".format(type(linhas_do_arquivo)))

#colocando a lista em ordem alfabética
linhas_do_arquivo.sort()

#Exibindo nossa lista, agora em ordem alfabética
print(linhas_do_arquivo)