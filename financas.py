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
