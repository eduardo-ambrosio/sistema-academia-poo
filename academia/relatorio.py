class Relatorio:
    def exibir(self, aluno):
        print("\n===== RELATÓRIO =====")
        print(f"Aluno: {aluno.nome}")
        print(f"Peso: {aluno.peso} kg")
        print(f"Meta de peso: {aluno.meta_peso} kg")
        print(f"Quantidade de treinos: {aluno.treinos}")