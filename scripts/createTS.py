##Criando uma Série Temporal Aleatória em Python

# Bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cria uma série temporal normalmente distribuída
np.random.seed (42) # para reproduzibilidade
myts = np.random.normal(size=252) # 252 meses (21 anos)

# Convertendo para série temporal com frequência mensal (12)
dates = pd.date_range (start='2004-05', end='2025-05', freq='ME')
myts_series = pd. Series (myts, index=dates)
myts_series.plot(title='Série Temporal Aleatória')
plt.show()