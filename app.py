qtd = 0
soma = 0
media = 0
valor = float(input("digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    valor = float(input("Digite um valor: "))

media = soma / qtd
print("\ntotal da soma:", soma)
print("\n qtd digitada: ", qtd)
print("\n media dos valores: ", media)