class HistoricoPeso:
    def __init__(self):
        self.__pesos = []

    def adicionar_peso(self, peso):
        self.__pesos.append(peso)

    def calcular_variacao(self):
        if len(self.pesos) >= 2:
            primeiro_peso = self.__pesos[0]
            ultimo_peso = self.__pesos[-1]
            return ultimo_peso - primeiro_peso
        return 0

    def __len__(self):
        return len(self.__pesos)

    @property
    def pesos(self):
        return self.__pesos