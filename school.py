# programa onde faz o cadastro de alunos de uma escola e depois confere as informações.
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['school']
collection = db['alunos']


def reg_aluno():
    nome = input("Digite o nome do Aluno: ")
    nascimento = input("Digite a data de nascimento: (dd/mm/yyyy) ")
    nome_mãe = input("Digite o nome da mãe: ")
    cidade = input("Digite a cidade onde mora: ")
    matricula = input("Digite o número da matrícula: ")
    nota = input("Média da nota: ")

    aluno = {
        "nome": nome,
        "nascimento": nascimento,
        "nome_mãe": nome_mãe,
        "cidade": cidade,
        "matricula": matricula,
        "nota": nota,
    }

    collection.insert_one(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")

def src_aluno():
    nome = input("Digite o nome do aluno que deseja buscar: ")
    aluno = collection.find_one({"nome": nome})
    
    if aluno:
        print(f"Dados do aluno {nome}" )
        print(f"Data de nascimento: {aluno['nascimento']}" )
        print(f"Nome da mãe: {aluno['nome_mãe']} ")
        print(f"Cidade onde mora: {aluno['cidade']} ")
        print(f"Matrícula: {aluno['matricula']} ")
        print(f"Nota medía: {aluno['nota']} ")
    else:
        print(f"Aluno {nome} não encontrado!")

while True:
    print("\n1. Cadastrar aluno")
    print("2. Buscar aluno")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        reg_aluno()
    elif opcao == "2":
        src_aluno()
    elif opcao == "3":
        print("Saindo do programa")
        break
    else:
        print("Opção inválida. Tente novamente.")                
