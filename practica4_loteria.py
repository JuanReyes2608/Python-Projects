import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('data/loteria.csv')

print(df.head())
#1. cuantos sorteos hay por año

df['Draw Date'] = pd.to_datetime(df['Draw Date']) # Convertir la columna 'Draw Date' a tipo datetime
df['Year'] = df['Draw Date'].dt.year # Extraer el año de la columna 'Draw Date' y crear una nueva columna 'Year'

sorteos_por_año = df['Year'].value_counts().sort_index() # Contar la cantidad de sorteos por año y ordenar por año
print('sorteos por año:' ,sorteos_por_año)
print("--------------------------------------------------")


#2. cual es el multiplicador mas frecuente
multiplicador_mas_frecuente = df['Multiplier'].value_counts().idxmax() # Contar la frecuencia de cada multiplicador 
print('multiplicador mas frecuente: ', multiplicador_mas_frecuente)
print("--------------------------------------------------")

#3. ¿Cuáles fueron los 5 sorteos con el multiplicador más alto?
sorteos_mas_alto = df.sort_values(by='Multiplier', ascending=False).head(5) # Ordenar los sorteos por multiplicador en orden descendente y seleccionar los primeros 5
print('los sorteos mas altos:', sorteos_mas_alto)
print("--------------------------------------------------")


#4. ¿Cómo ha cambiado la frecuencia de multiplicadores altos (por ejemplo, 5 o más) a lo largo de los años?
frecuencia_multiplicadores_altos = df[df['Multiplier'] >= 5].groupby('Year').size() # Filtrar los sorteos con multiplicador 4 o más, agrupar por año y contar la cantidad de sorteos por año
print('Frecuencia de multiplicadores altos:', frecuencia_multiplicadores_altos)
print("--------------------------------------------------")


#5. ¿Cuántos sorteos se realizaron por mes en el último año disponible?
sorteos_ultimo_año = df[df['Year'] == df['Year'].max()] # Filtrar los sorteos del último año disponible
sorteos_ultimo_año_por_mes = sorteos_ultimo_año['Draw Date'].dt.month.value_counts().sort_index() # Contar la cantidad de sorteos por mes y ordenar por mes
print('sorteos realizados en el ultimo año:', sorteos_ultimo_año)
print(sorteos_ultimo_año_por_mes)
print("--------------------------------------------------")


#6. ¿Cómo se distribuyen los multiplicadores en todos los sorteos?
distribucion_multiplicadores = df['Multiplier'].value_counts().sort_index() # Contar la frecuencia de cada multiplicador y ordenar por multiplicador
print('distribución de multiplicadores:', distribucion_multiplicadores)
print("--------------------------------------------------")


#7. ¿En qué fecha ocurrió el primer y el último sorteo registrado?
primer_sorteo = df['Draw Date'].min() # Obtener la fecha del primer sorteo
ultimo_sorteo = df['Draw Date'].max() # Obtener la fecha del último sorteo
print('primer sorteo:', primer_sorteo)
print('ultimo sorteo:', ultimo_sorteo)
print("--------------------------------------------------")


#8. ¿Cuáles son los números ganadores más repetidos?
df['Winning Numbers'] = df['Winning Numbers'].str.split() # Dividir los números ganadores en listas
todos_los_numeros = df['Winning Numbers'].explode() # Expandir las listas en filas individuales
numeros_mas_repetidos = df['Winning Numbers'].explode().value_counts()
print('El numero mas repetido es el:', numeros_mas_repetidos)
print("--------------------------------------------------")


#9. ¿Cuál es el promedio del multiplicador por año?
promedio_multiplicador_por_año = df.groupby('Year')['Multiplier'].mean() # Agrupar por año y calcular el promedio del multiplicador
promedio_multiplicador_por_año = promedio_multiplicador_por_año.round(2) # Redondear a 2 decimales
print('promedio del multiplicador por año:', promedio_multiplicador_por_año)
print("--------------------------------------------------")


# visualizacion de sorteos por año 
sorteos_por_año.plot(kind='bar', figsize = (10,6), color = 'skyblue')
plt.title('Cantidad de Sorteos por Año')
plt.xlabel('año')
plt.ylabel('Cantidad de sorteos')
plt.show()

# visualizacion de frecuencia de multiplicadores altos
frecuencia_multiplicadores_altos.plot(kind='bar', figsize=(10,6), color='orange')
plt.title('Frecuencia de Multiplicadores Altos (5 o más) por Año')
plt.xlabel('Año')
plt.ylabel('Cantidad de Sorteos con Multiplicador Alto')
plt.show()