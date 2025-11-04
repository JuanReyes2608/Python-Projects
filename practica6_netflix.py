import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv ('data/netflix_cleaned.csv')
print(df.head())
print('/'*100)
print(df.columns)
print('/'*100)
print(df.info())
print('/'*100)
print(df.describe(include='all'))
print('/'*100)
print(df.nunique())
print('/'*100)

df['release_year'] = df['release_year'].astype('Int64')
df['release_month'] = df['release_month'].astype('Int64')

print(df.info())
print('-'*100,'\n')

#EDA 

#1. Que tipo de contenido hay mas, peliculas o series?
mayor_contenido = df['category'].value_counts()
print('la categoria con mas contenido es:', mayor_contenido.idxmax())
print(mayor_contenido)
print('-'*100,'\n')

#2. porcentaje de Peliculas vs Series
porcentaje_categorias = mayor_contenido / mayor_contenido.sum() *100
print(porcentaje_categorias)
print('-'*100,'\n')

#3. Cual es es pais con mayor cantidad de producciones?
pais_mayor_producciones = df['country'].value_counts().head(10)
print(pais_mayor_producciones)
print('-'*100,'\n')

#4. distribucion de ratings
distribucion_rattings = df['rating'].value_counts()
print(distribucion_rattings)
print('-'*100,'\n')
porcentaje_ratings = distribucion_rattings / distribucion_rattings.sum() * 100
print(porcentaje_ratings)
print('-'*100,'\n')

#5. cuantos titulos se lanzaron por año?
titulos_por_año = df['release_year'].value_counts().sort_index(ascending=False)
print(titulos_por_año)
print('-'*100,'\n')

#6. promedio de duracion por tipo de contenido 
promedio_duracion = df.groupby('category')['duration_int'].mean()
print(promedio_duracion)
print('-'*100,'\n')

#7. top 10 generos mas comunes
generos = df['type'].dropna().str.split(',').explode()          # split convierte un string en una lista.   
#                                                                 explode convierte listas dentro de una columna en filas separadas
all_generos =  generos.str.strip()                              # strip limpia espacios antes y después de cada género.
contar_generos = all_generos.value_counts().head(10)
print(contar_generos)
print('-'*100,'\n')

#Visualización
#1. Distribucion de titulos por categoria 
plt.figure(figsize=(6,4))
plt.bar(mayor_contenido.index, mayor_contenido.values) 
plt.title('Distribución de titulos por categoría')
plt.xlabel('categoria')
plt.ylabel('contenido')
plt.show()


#2. titulos por año
plt.bar(titulos_por_año.index, titulos_por_año.values, color="#1fb47d")
plt.title('Titulos por año')
plt.xlabel('año')
plt.ylabel('Cantidad de titulos')
plt.show()

#3. paises con mas producciones 
plt.figure(figsize=(13,4))
plt.barh(pais_mayor_producciones.index, pais_mayor_producciones.values)
plt.title('top 10 Paises con mayores producciones')
plt.xlabel('pais')
plt.ylabel('# de producciones')
plt.show()

#4. ratings mas comunes 
plt.figure(figsize=(16,4))
plt.bar(distribucion_rattings.index, distribucion_rattings.values)
plt.title('porcentaje de ratings')
plt.xlabel('ratings')
plt.ylabel('cantidad de titulos')

plt.show()

#5. distribución por genero 
plt.figure(figsize=(22,4))
plt.bar(contar_generos.index, contar_generos.values)
plt.title('top 10 generos mas populares')
plt.xlabel('genero')
plt.ylabel('cantidad')
plt.show()