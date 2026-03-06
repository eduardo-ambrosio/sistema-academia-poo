class PlanoTreino:
    def __init__(self, objetivo, nivel):
        self.objetivo = objetivo
        self.nivel = nivel

    def __str__(self):
        return f"{self.objetivo} (Nível {self.nivel})"