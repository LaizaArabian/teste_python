arquivo = open("texto.txt", "w")

arquivo.write("Curso Python\n")
arquivo.write("alalallala")
arquivo.close()

# leitura do arq
leitura = open("texto.txt", "r")
print(leitura.read())
leitura.close()