class ContaBancaria:
    def __init__(self, id, titular, saldo):
        # construtor: inicializa os atributos da conta
        self.id = id
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        # define como a conta é exibida quando usada em print()
        return f'A conta: {self.id}, de: {self.titular}, tem: {self.saldo:.2f} R$ de saldo'

    def deposito(self, valor):
        # adiciona o valor ao saldo da conta
        self.saldo = self.saldo + valor

    def saque(self, valor):
        # verifica se há saldo suficiente antes de sacar
        if valor <= self.saldo:
            self.saldo = self.saldo - valor  # desconta o valor do saldo
            print(f'Saque realizado no valor de: {valor:.2f}, na conta: {self.id}, de: {self.titular}')
        else:
            print(f'Saldo insuficiente para realizar o saque de: {valor:.2f}')


# cria uma conta bancária com id, titular e saldo inicial
c1 = ContaBancaria(1122, "Antonio", 30000)
print(c1)          # mostra os dados da conta
c1.saque(1000)      # tenta sacar 1000
print(c1)           # mostra os dados atualizados da conta