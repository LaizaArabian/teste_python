def lernotas():
    n = float(input("digite uma nota: "))
    return n

def resultado(n1,n2):
    media = (n1+n2)/2
    print("nota 1: ", n1)
    print("nota 2: ", n2)
    print("media: ", media, "resultado: ", end="") # serve pra mostrar na mesma linha
    if media>=7:
        print("Aprovado") 
    else: 
        print("Reprovado") 

a = lernotas()
b = lernotas()
resultado(a,b) # pega os valores de n1,n2 e joga pra a,b