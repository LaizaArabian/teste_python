class Main:
    pass

print("------ TESTE ------")

from cliente import Cliente
from conta import Conta

c1 = Cliente("João", "1123456789", "01")
conta = Conta(c1.nome, 1010, 0) 

print("nome: ", c1.nome, "\ntelefone: ", c1.telefone, "\ncpf: ", c1.cpf)
print(conta.titular,"numero da conta: ", conta.numero, "\nsaldo: ", conta.saldo)