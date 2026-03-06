from aluno import Aluno
from regras import Regras
from relatorio import Relatorio
from plano_treino import PlanoTreino

def main():
    nome = input("Digite o nome do aluno: ")
    peso = float(input("Digite o peso (kg): "))
    meta_peso = float(input("Digite seu meta peso (kg): "))
    treinos = int(input("Digite a quantidade de treinos semanais:"))
    objetivo = input("Digite o objetivo do plano (ex: emagrecimento, hipertrofia): ")
    nivel = input("Digite o nível do plano (ex: iniciante, intermediário, avançado): ")

    regras = Regras()
    # validações
    regras.peso(peso)
    regras.meta_peso(meta_peso)
    regras.treinos(treinos)

    aluno = Aluno(nome, peso, meta_peso)
    plano = PlanoTreino(objetivo, nivel)
    aluno.definir_plano(plano)

    # treinos só via método
    for i in range(treinos):
        aluno.registrar_treino()

    while True:
        resposta = input("\nDeseja registrar uma nova pesagem? (s/n): ").strip().lower()
        if resposta == 's':
            novo_peso = float(input("Digite o peso atualizado (kg): "))
            aluno.atualizar_peso(novo_peso)
            print("✔️ Peso atualizado no histórico!")
        elif resposta == 'n':
            print("Encerrando pesagens e gerando relatório...")
            break
        else:
            print("Opção inválida! Digite 's' para sim ou 'n' para não.")

    relatorio = Relatorio()
    relatorio.exibir(aluno)


if __name__ == "__main__":
    main()