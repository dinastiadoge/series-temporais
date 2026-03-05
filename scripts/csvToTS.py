# Importando uma série temporal de um arquivo no formato CSV
# Bibliotecas
import csv
import pandas as pd
import matplotlib.pyplot as plt

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            linhas = list(leitor_csv)
        return linhas
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        return None
# Exemplo de uso:
nome_arquivo = './scripts/arquivos/monthly-car-sales.csv' # Substitua pelo nome da pasta e arquivo CSV
dados = ler_csv(nome_arquivo)

data = [sb[1] for sb in dados[1:]] # Pula cabeçalho, obtém apenas a variável valor
values = [float(i) for i in data] # Transforma em lista de float
stValues = pd.period_range(start='1884', end='1991', freq='Y')
myts_series = pd.Series(values, index=stValues)
myts_series.plot(title='Monthly Car Sales')
plt.show()