import pandas as pd
import numpy as np

df_clima =  pd.read_csv("archivos_necesarios/clima.csv")

print(df_clima)

promedio_por_ciudad = df_clima.groupby('Ciudad')['Temperatura'].mean()

print(promedio_por_ciudad)