import pandas as pd

df_ventas =  pd.read_csv("archivos_necesarios/ventas.csv")

#print(df_ventas)

total_productos = df_ventas.groupby("Producto").sum()

#print(total_productos)

producto_mas_vendido = total_productos["Cantidad"].idxmax()

print(f"El producto con mas ventas es: {producto_mas_vendido}")