class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0
        self.numero = numero
        self.titular = titular

        # get - pega os valor e envia
        # set - recebem os valores

    @property # função usada para obter valor de um atributo
    def saldo(self):
        return self._saldo
    
    @saldo.setter # recebe
    def saldo(self, saldo):
        if (saldo < 0):
            print("o saldo nao pode ser negativo!")
        else:
            self._saldo = saldo
    