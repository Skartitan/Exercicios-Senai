class Conta:
    def __init__(self,saldo):
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def get_saldo(self):
        print(f"Saldo atual: {self.__saldo}")

minha_conta = Conta(100)
minha_conta.depositar(50)
minha_conta.get_saldo()

outra_conta = Conta(1000)
outra_conta.get_saldo()