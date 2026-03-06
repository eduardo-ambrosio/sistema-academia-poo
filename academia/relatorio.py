class Relatorio:
    def exibir(self, aluno):
        print("\n===== RELATÓRIO =====")
        print(f"Aluno: {aluno.nome}")
        print(f"Peso: {aluno.peso} kg")
        print(f"Meta de peso: {aluno.meta_peso} kg")
        print(f"Quantidade de treinos: {aluno.treinos}")
        print(f"Total de pesagens: {len(aluno.historico)}")
        print(f"Variação de peso: {aluno.historico.calcular_variacao():.2f} kg")
        print(f"Diferença percentual para a meta: {aluno.percentual_para_meta()}%")
        if aluno.plano is not None:
            print(f"Plano de Treino: {aluno.plano}")
        else:
            print("Plano de Treino: Nenhum plano definido.")