class Estudante:
    escola = "Dio"
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nasc(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# aluno_1 = Estudante("Guilherme", 12)
# aluno_2 = Estudante("Gustavo", 45)

p = Estudante.criar_de_data_nasc(2003, 10, 4, "Daniel")

print(p.nome, p.idade)

print(es.e_maior_idade(15))
