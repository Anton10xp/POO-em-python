class Pessoa:
    def __init__(self, nome, idade):
        # atributos protegidos (uso interno da classe e subclasses)
        self._nome = nome
        self._idade = idade

    def get_nome(self):
        # retorna o nome (getter)
        return self._nome

    def set_nome(self, novo):
        # altera o nome (setter)
        self._nome = novo

    def get_idade(self):
        # retorna a idade (getter)
        return self._idade

    def set_idade(self, nova):
        # altera a idade (setter)
        self._idade = nova

    def faz_aniversario(self):
        # aumenta a idade em 1 usando os próprios getters/setters
        self.set_idade(self.get_idade() + 1)

    def __str__(self):
        # define como o objeto aparece em print()
        return f'Nome: {self.get_nome()}, idade: {self.get_idade()}'


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)  # reaproveita o construtor de Pessoa
        self._curso = curso  # atributo protegido, consistente com os getters/setters
        self._turma = turma  # atributo protegido, consistente com os getters/setters

    def set_curso(self, novo):
        self._curso = novo

    def set_turma(self, nova):
        self._turma = nova

    def get_curso(self):
        return self._curso

    def get_turma(self):
        return self._turma


# cria um aluno (herda nome, idade de Pessoa + curso e turma)
aluno1 = Aluno("Ana", 19, "BIA", "Turma 1")

print(aluno1.get_nome())  # acessa método herdado de Pessoa

aluno1.faz_aniversario()  # usa método herdado para aumentar a idade
print(aluno1.get_idade())


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)  # reaproveita o construtor de Pessoa

        self._especialidade = especialidade
        self._nivel = nivel

    def get_especialidade(self):
        return self._especialidade

    def get_nivel(self):
        return self._nivel

    def set_especialidade(self, nova):
        self._especialidade = nova

    def set_nivel(self, nova):
        self._nivel = nova

    def dar_aula(self):
        # mostra os dados do professor, incluindo os herdados de Pessoa
        print(f"Nome do professor: {self.get_nome()}, idade do professor: {self.get_idade()}, especialidade do professor: {self.get_especialidade()}, nivel do professor: {self.get_nivel()}")


# cria um professor (herda nome, idade de Pessoa + especialidade e nivel)
professor1 = Professor("Jonas", 30, "Visão computacional", "Doutorado")

# Printa a função dar_aula aonde todas as informações do objeto estão presentes, provando que o professor realmente herdou as funções do Aluno que por si só Herdou as funções de Pessoa.
print(professor1.dar_aula())