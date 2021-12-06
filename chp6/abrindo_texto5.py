#usando a função open para criar um objeto do tipo arquivo
arquivo = open("i_can_see.txt")

#printando uma linha do arquivo
print(arquivo.readlines())
arquivo.close()