import pandas as pd

df_calificaiones = pd.read_csv("archivos_necesarios/calificaciones.csv")

#print(df_calificaiones)

materia_promedio = df_calificaiones.groupby("Materia")["Calificación"].mean()

#print(materia_promedio)

promedio = df_calificaiones.groupby("Estudiante")["Calificación"].mean()

estudiante_mejor_promedio = promedio.idxmax()
mejor_promedio_valor = promedio.max()

#print(f"el estudiante {estudiante_mejor_promedio} tiene el mejor promedio de: {mejor_promedio_valor}")

promedios_estudiantes = promedio.sort_values()

#print(promedios_estudiantes)

promedio_mayor_85 = (promedio > 85).sum()

#print(promedio_mayor_85)

materia_calificaciones = df_calificaiones["Materia"].value_counts().idxmax()
cantidad_calificaciones = df_calificaiones["Materia"].value_counts().max()

#print(f"Materia con más calificaciones: {materia_calificaciones}")

#print(cantidad_calificaciones)

promedio_mas_bjo = promedio.sort_values().head(5)
print(promedio_mas_bjo)
