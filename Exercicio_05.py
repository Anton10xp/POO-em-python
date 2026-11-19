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