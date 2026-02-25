from aluno import Aluno
from regras import Regras
from relatorio import Relatorio

def main():
    nome = input("Digite o nome do aluno: ")
    peso = float(input("Digite o peso (kg): "))
    meta_peso = float(input("Digite seu meta peso (kg): "))
    treinos = int(input("Digite a quantidade de treinos semanais:"))

    regras = Regras()
    # validações
    regras.peso(peso)
    regras.meta_peso(meta_peso)
    regras.treinos(treinos)

    aluno = Aluno(nome, peso, meta_peso)

    # treinos só via método
    for i in range(treinos):
        aluno.registrar_treino()

    relatorio = Relatorio()
    relatorio.exibir(aluno)


if __name__ == "__main__":
    main()