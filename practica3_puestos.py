# En esta practica voy a realizar un analisis de datos sobre ganadores de lotería. el primer pasó será cargar los datos.
import pandas as pd # la libreria nos ayudara a cargar y manipular los datos

df = pd.read_csv('data/puestos_directivos.csv') # hacemos que se carguen los datos del archivo CSV
print(df.head())  # Muestra las primeras 5 filas de los datos 

print()  # Salto de línea

print('informaci[on del DataFrame:')
df.info()  # Muestra un resumen de la información del DataFrame

df.describe()  # Muestra estadísticas descriptivas de las columnas numéricas

# paso 2: analisis de datos
#1. ¿Cuál es el porcentaje promedio de mujeres y hombres en puestos directivos por año?
promedio_por_año = df.groupby('anio')[['prct_mujeres','prct_hombres']].mean()# agrupamos los datos por año y calculamos el promedio de mujeres y hombres
print(promedio_por_año)  # mostramos el promedio por año
print()

#2.¿Qué entidad tuvo el mayor porcentaje de mujeres en puestos directivos en 2024?
mayor_entidad_2024 = df[df['anio'] == 2024].loc[df[df['anio'] == 2024]['prct_mujeres'].idxmax()]  # filtramos los datos para el año 2024 y encontramos la entidad con el mayor porcentaje de mujeres
print(mayor_entidad_2024)  # mostramos la entidad con el mayor porcentaje de mujeres en el año 2024
print()

#3.¿Cómo ha cambiado el total de puestos directivos en Ciudad de México a lo largo de los años?
cdmx = df[df['entidad'] == 'Ciudad de México']
total_cdmx = cdmx.groupby('anio')['total'].sum()  # filtramos los datos para la Ciudad de México y sumamos el total de puestos directivos por año
print(total_cdmx)  # mostramos el total de puestos directivos en la Ciudad de México por año
print()

#4. ¿Qué entidades han mostrado mayor crecimiento en el porcentaje de mujeres desde 2005 hasta 2024?
crecimiento_mujeres = df[df['anio']].isin([2005,2024])
