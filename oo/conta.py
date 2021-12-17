class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo de {self.__saldo} do {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_saque):
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel_saque


    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print (f"Saque efetuado com sucesso no valor de {valor}")
        else:
            print (f"O valor {valor} do saque é maior que seu limite!")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite