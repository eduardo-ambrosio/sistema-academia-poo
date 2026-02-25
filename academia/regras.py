class Regras:
    def peso(self, peso):
        if peso < 0:
            raise ValueError("Peso não pode ser negativo")
        else:
            print(f"Seu peso é {peso} kg ")

    def meta_peso(self, meta_peso):
        if meta_peso <= 0:
            raise ValueError("Sua meta de peso tem que ser maior que 0")
        else:
            print(f"Sua meta de peso é {meta_peso} kg ")

    def treinos(self, treinos):
        if treinos < 0:
            raise ValueError("A quantidade de treinos não pode ser negativo")
        else:
            print(f"A quantidade de treinos são {treinos} ")