class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def __str__(self):
        return f"{self.nome} - {self.idade} anos"