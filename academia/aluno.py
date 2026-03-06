from histórico import HistoricoPeso

class Aluno:
    def __init__(self, nome, peso, meta_peso):
        self.nome = nome
        self.peso = peso
        self.meta_peso = meta_peso
        self.__treinos = 0
        self.historico = HistoricoPeso()
        self.historico.adicionar_peso(peso)
        self.plano = None

    @property
    def treinos(self):
        return  self.__treinos

    def registrar_treino(self):
        self.__treinos += 1

    def atualizar_peso(self, novo_peso):
        self.peso = novo_peso
        self.historico.adicionar_peso(novo_peso)

    def definir_plano(self, plano_treino):
        self.plano = plano_treino

    def percentual_para_meta(self):
        diferenca = abs(self.peso - self.meta_peso)
        percentual = (diferenca / self.meta_peso) * 100
        return round(percentual, 2)