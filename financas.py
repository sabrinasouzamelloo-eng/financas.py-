import json
import os
from datetime import datetime

arquivo = "lancamentos.json"

def carregar():
    if not os.path.exists(arquivo):
       return []

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
          return json.loads(f.read())
    except Exception:
        return []
def salvar(lancamentos):
    try:
        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(json.dumps(lancamentos, indent=4, ensure_ascii=False))
    except Exception:
        pass

def registrar_lancamentos(lancamentos):
    print(" Registro Novo")
    tipo = input("Receita ou Despesa: ").strip().lower()

    try:
        valor = float(input("Digite o valor: "))
    except ValueError:
        print("Coloque um valor correto viado!!!")
        return

    categoria = input("Digite a categoria do Gasto ou Recebimento: ").strip()
    descricao = input("Digite um resumo do que: ").strip()

    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%s")

    nova_info = {
        "data": data_atual,
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao
    }

    lancamentos.append(nova_info)
    salvar(lancamentos)
    print("Info lançada com sucesso.")

def mostrar_extrato(lancamentos):
    print("\n" + "="*20 + " Extrato " + "="*20)
    if not lancamentos:
        print("Nenhuma info encontrada.")
        print("="*64)
        return

    for item in lancamentos:
        print(f"data: {item["data"]} | tipo: {item["tipo"]} | valor: {item["valor"]:.2f} | caegoria: {item["categoria"]} | descricao: {item["descricao"]})
    print("="*64)

def calcular_saldo(lancamentos):
    total_receitas = sum(item["valor"] for item in lancamentos if item["tipo"] == "receitas")
    total_despesas = sum(item["valor"] for item in lancamentos if item["tipo"] == "despesas")
    saldo_total = total_receitas - total_despesas

    por_categoria = {}
    for item in lancamentos:
        cat = item["categoria"]
        if item["tipo"] == por_categoria.get(cat, 0) - item["valor"]
        else:
            por_categoria[cat] == por_categoria.get(cat, 0) + item["valor"]
        return saldo_total, total_receitas, total_despesas, por_categoria


def gerar_texto_relatorio(lancamentos):
    saldo, receitas, despesas, categorias = calcular_saldo(lancamentos)

    texto = "=" * 15 + " RELATÓRIO FINANCEIRO " + "=" * 15 + "\n"
    texto += f"Total de Receitas: R$ {receitas:.2f}\n"
    texto += f"Total de Despesas: R$ {despesas:.2f}\n"
    texto += f"Saldo Total      : R$ {saldo:.2f}\n"
    texto += "-" * 52 + "\n"
    texto += "Saldo por Categoria:\n"

    if not categorias:
        texto += "Categoria não registrada.\n"
    for cat, val in categorias.items():
        texto += f" - {cat}: R$ {val:.2f}\n"
    texto += "=" * 52 + "\n"
    return texto


def exibir_relatorio(lancamentos):
    print("\n" + gerar_texto_relatorio(lancamentos))


def exportar_relatorio(lancamentos):
    try:
        conteudo = gerar_texto_relatorio(lancamentos)
        with open('relatorio.txt', 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print("\n[SISTEMA] Arquivo 'relatorio.txt' gerado com sucesso!")
    except Exception:
        print("[SISTEMA] Erro ao exportar relatório.")


def menu():
    lancamentos = carregar()

    while True:
        print("\n=== APP DE FINANÇAS PESSOAIS ===")
        print("1 - REGISTRAR")
        print("2 - VER EXTRATO")
        print("3 - RELATÓRIO")
        print("4 - EXPORTAR")
        print("5 - SAIR")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            registrar_lancamentos(lancamentos)
        elif opcao == '2':
             mostrar_extrato(lancamentos)
        elif opcao == '3':
            exibir_relatorio(lancamentos)
        elif opcao == '4':
            exportar_relatorio(lancamentos)
        elif opcao == '5':
            print("Encerrando o programa. Até logo!")
            break