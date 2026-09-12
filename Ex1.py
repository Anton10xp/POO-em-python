class Pessoa:
    def __init__(self): #Metodo construtor
        '''Atributos de intancia: '''
        self.nome = ""
        self.idade = 0

    #Métodos da instacia:
    def aniversario(self):
        self.idade = self.idade + 1


    def mensagem(self):
        return f'Nome da Pessoa: {self.nome}, tem {self.idade}, anos de idade.'

#declaração de objetos:
#aqui eu estou declarando os meus objetos aonde eu passo para cada um o meu construtor, dou um nome para eles chamando o meu metodo nome e idade dando a idade para ele.
Pessoa1 = Pessoa()
Pessoa1.nome = "Maria"
Pessoa1.idade = 17
'''Depois eu criei uma função chamada aniversario aonde eu coloquei o meu atributo idade + 1, então eu chamei esta função'''
Pessoa1.aniversario()    
'''Depois aqui eu chamei a minha função do metodo de instacia aonde esta função é responsavel por retornar uma mensagem com o nome e a idade dos objetos'''
print(Pessoa1.mensagem())

'''Aqui eu tambem declarei outro objeto só que nao chamei a função aniversario, ou seja o objeto permanece com a idade que eu tinha declarado antes'''
Pessoa2 = Pessoa()
Pessoa2.nome = "Antonio"
Pessoa2.idade = 19

print(Pessoa2.mensagem())