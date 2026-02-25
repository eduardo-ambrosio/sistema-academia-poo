class Aluno:
    def __init__(self, nome, peso, meta_peso):
        self.nome = nome
        self.peso = peso
        self.meta_peso = meta_peso
        self.__treinos = 0

    @property
    def treinos(self):
        return  self.__treinos

    def registrar_treino(self):
        self.__treinos += 1