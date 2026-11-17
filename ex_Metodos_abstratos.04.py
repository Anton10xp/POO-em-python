from abc import abstractmethod, ABC

class Funcionario(ABC):
    def __init__(self, nome, salario_base, cpf):
        self.nome = nome

        self.__salario_base = 0
        self.salario_base = salario_base
        
        self.__cpf = 0
        self.cpf = cpf

    @property
    def salario(self):
        return self.__salario_base


    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo):
        if not isinstance(novo, str):
            print("O cpf deve ser informado com texto")
            return

        self.__cpf = novo

    @salario.setter
    def salario(self, novo):
        if novo < 0:
            print("O salario noa pode ser negativo") 
            return

        self.__salario_base = novo


    @abstractmethod
    def salario_final(self, quantidade):
        pass


    @abstractmethod
    def __str__(self):
        pass


class Gerente(Funcionario):
    def __init__(self, nome, salario_base, cpf, cargo, comisao):
        super().__init__(nome, salario_base, cpf)
        self.__cargo = ""
        self.cargo = cargo
        self.comisao = comisao

        @property
        def cargo(self):
            return self.__cargo

        @cargo.setter
        def cargo(self, novo):
            if novo.strip() == "":
                print("O Cargo não pode estar vazio")
                return

            self.__cargo = novo


    def salario_final(self, quantidade):
        return (self.comisao * quantidade) + self.salario_base


    def __str__(self):
        return (f"Nome {self.nome}, cpf: {self.cpf}, cargo: {self.cargo}, salario Final: {self.salario_final(10)}")


class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, cpf, cargo, comisao):
        super().__init__(nome, salario_base, cpf)
        self.__cargo = ""
        self.cargo = cargo
        self.comisao = comisao

        @property
        def cargo(self):
            return self.__cargo

        @cargo.setter
        def cargo(self, novo):
            if novo == "":
                print("O cargo deve ser preenchido")
                return
            self.__cargo = novo


    def salario_final(self, quantidade):
            return (self.comisao * quantidade) + self.salario_base


    def __str__(self):
        return (f"Nome: {self.nome}, cpf: {self.cpf}, Cargo: {self.cargo}, Salario base: {self.salario_base} salario Final: {self.salario_final(0)}")




if __name__ == "__main__":

    v1 = Vendedor ("Gugu", 7700, '000000000000', "Gerente de vendas", 25.0)

    g1 = Gerente("Antonio", 15000, "021031298124", "CEOFO", 12000)


    print(g1)