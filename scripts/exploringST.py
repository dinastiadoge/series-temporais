
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.api import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm
from statsmodels.datasets import sunspots

data = sunspots.load_pandas().data
print("Data:",data)
print("Type:",type(data))   
print("Max:",data.max())
print("Min:",data.min())
print("Mean:",data.mean())
print("Median:",data.median())
print("Length:",len(data))
print("Describe:",data.describe())
print("Last:",data.last_valid_index())
print("First:",data.first_valid_index())
#correlation uses the last 
autocorr = data.corr().lene()
print("Autocorrelation:",autocorr)

