from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario_base):
        self.__nome = ""
        self.__salario_base = 0

        self.nome = nome
        self.salario_base = salario_base

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo):
        if not isinstance(novo, str):
            raise TypeError("O nome deve ser um texto")

        if not novo.strip():
            raise ValueError("O nome nao pode ficar vazio")

        self.__nome = novo.strip()

    @property
    def salario_base(self):
        return self.__salario_base

    @salario_base.setter
    def salario_base(self, novo):
        if novo < 0:
            raise ValueError("O Salario nao pode ser naegativo")
            
        else:
            
            self.__salario_base = novo

    @abstractmethod
    def salario_final(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

        if bonus < 0:
            raise ValueError("O bonus nao pode ser negativo")

        else:
            self.__bonus = bonus

    @property
    def bonus(self): 
        return self.__bonus


    def salario_final(self):
        return self.salario_base + self.bonus


class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, comisao, quantidade):
        super().__init__(nome, salario_base)                                

        if comisao < 0:
            raise ValueError("A comissao nao pode ser negatriva")

        else:

            self.__comisao = comisao

        @property
        def comisao(self):
            return self.__comisao


        if type(quantidade) is not int:
            raise TypeError("A quantidade deve ser um numero inteiro")
        
        self.__quantidade = quantidade

        if quantidade < 0:
            raise ValueError("O quantidade nao poder ser negativa")

        self.__quantidade = quantidade

        @property
        def quantidade(self):
            return self.__quantidade

        
    def salario_final(self):
        return self.salario_base + self.comisao * self.quantidade

    