# Scripts

Pasta destinada aos scripts Python utilitários e de apoio à disciplina de Séries Temporais.

## Estrutura sugerida

Organize os scripts por tema ou funcionalidade:

```
scripts/
├── exploracao/
│   └── analise_exploratoria.py
├── modelos/
│   ├── arima.py
│   └── sarima.py
├── visualizacao/
│   └── plots.py
└── utils.py
```

## Dependências comuns

- `pandas`
- `numpy`
- `matplotlib`
- `statsmodels`
- `scikit-learn`
- `ipykernel`

## Boilerplate de dependências
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm
```
## Criação de ambientes

# Create venv
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# Install packages
pip install pandas numpy matplotlib statsmodels