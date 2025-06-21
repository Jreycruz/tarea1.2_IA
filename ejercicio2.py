import pandas as pd
import numpy as np

df_clima =  pd.read_csv('archivos_necesarios/clima.csv')

#print(df_clima)

promedio_por_ciudad = df_clima.groupby('Ciudad')['Temperatura'].mean()

#print(promedio_por_ciudad)

temp_max = df_clima['Temperatura'].idxmax()
temp_min = df_clima['Temperatura'].idxmin()

#print(temp_max)

ciudad_temp_max = df_clima.loc[temp_max, 'Ciudad']
ciudad_temp_min = df_clima.loc[temp_min, 'Ciudad']

#print("Ciudad con la temperatura más alta:", ciudad_temp_max)
#print("Ciudad con la temperatura más alta:", ciudad_temp_min)

registros_mayor_30 = (df_clima['Temperatura'] > 30).sum()

print('registrso mayores a 30:', registros_mayor_30)