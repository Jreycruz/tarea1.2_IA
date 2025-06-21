import pandas as pd

df_ventas =  pd.read_csv("archivos_necesarios/ventas.csv")

#print(df_ventas)

total_productos = df_ventas.groupby("Producto").sum()

producto_mas_vendido = total_productos["Cantidad"].idxmax()

precio_promedio = df_ventas[df_ventas.Producto == "Monitor"]["Precio_Unitario"].mean()
#print(total_productos)
print(f"El producto con mas ventas es: {producto_mas_vendido} con un precio promedio de: {precio_promedio}")

#print(precio_promedio)
