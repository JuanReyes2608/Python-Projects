import pandas as pd 
import re

df = pd.read_csv('data/Netflix Dataset.csv')


#1. identificar columnas con muchos nulos, formatos de fecha y patrones
print('1. muestra las primeras 5 filas.' , '\n' ,df.head()) 
print('-' * 60)

print('2. muestra información sobre el DataFrame.', '\n' ,df.info()) 
print('-' * 60)

print('3. cuenta las filas y columnas que tiene el DataFrame.', '\n', df.shape) 
print('-' * 60)

print('4. muestra estadísticas descriptivas de las columnas numéricas.', '\n', df.describe()) 
print('-' * 60)

print('5. muestra la cantidad de valores nulos por columna.', '\n', df.isnull().sum()) 
print('-' * 60)

print('6. muestra la cantidad de valores únicos por columna.', '\n', df.nunique()) 
print('-' * 60)

#2. normalizar nombres de columnas
df.columns = (df.columns .str.strip() # eliminar espacios en blanco al inicio y final
              .str.lower()) # convertir a minúsculas

print(df.columns) # muestra los nombres de las columnas
print('-' * 40)

#3. limpieza de datos 
#3.1 manejo de valores nulos
print ('/'*60)
print ('valores nulos por culumna:')
print(df.isnull().sum())

df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')

df = df.dropna(subset=['release_date', 'rating'])

print("\nDespués de la limpieza:")
print(df.isnull().sum())
print('-' * 60)

#3.2 Parsear fechas 
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce') # convertir a datetime, los errores se convierten en NaT']
df['release_year'] = df['release_date'].dt.year # extraer el año de la fecha de lanzamiento
df['release_month'] = df['release_date'].dt.month # extraer el mes de la fecha de lanzamiento
nat_count = df['release_date'].isnull().sum()
print('-' * 60)

#3.3 limpieza de columna 'duration'

print('Valores únicos en la columna duration antes limpiar:')
print(df['duration'].unique()[:10])

df['duration_int'] = df['duration'].str.extract(r'(\d+)').astype(int) # extraer el número 
df['duration_unit'] = df['duration'].str.extract(r'([a-zA-Z]+)') # extraer solo letras

df['duration_unit'] = df['duration_unit'].replace({
    'Seasons': 'Season',
    'Season': 'Season',
    'min': 'min'
})  # Normalizar Duration_Unit

# Validar cambios
print("\nRevisión después de la limpieza:")
print(df[['duration', 'duration_int', 'duration_unit']].head(10))
print('-' * 60)

#3.4 limpieza y estandarizacion de 'rating' 
print('valores unicos de Rating antes de limpiar:')
print(df['rating'].unique())

rating_replacements = {
    'TVMA': 'TV-MA',
    'TV_14': 'TV-14',
    'TVY7': 'TV-Y7',
    'TVY': 'TV-Y',
    'Tv-Ma': 'TV-MA',
    'NR': 'Not Rated',
    'UNRATED': 'Not Rated',
    'UR': 'Not Rated'
}

# 3.4.1 Aplicar la limpieza
df['rating'] = df['rating'].replace(rating_replacements)

# 3.4.2 Validar resultado
print("\nValores únicos después de limpiar:")
print(df['rating'].unique())
print('-' * 60)

#3.5 manejar valores duplicados 
duplicados = df[df.duplicated(subset=['show_id'])]
print(f"Cantidad de duplicados encontrados: {duplicados.shape[0]}")
duplicados
df = df.drop_duplicates(subset=['show_id'], keep='first')

print(df.shape)

#4. guardar todo el dataframe limpio para la visualizacion de datos

df.to_csv('data/netflix_cleaned.csv', index= False)