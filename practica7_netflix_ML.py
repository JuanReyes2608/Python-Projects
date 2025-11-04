import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv('data/netflix_cleaned.csv')

#1. preparar las columnas 
print(df.columns)
df_ml = df[['category','release_year','rating','duration','type']].copy()


#1.1 Columna 'duration'
df_ml['duration_type'] = df_ml['duration'].str.extract('([A-Za-z]+)')
df_ml['duration_num'] = df_ml['duration'].str.extract(r'(\d+)').astype('float')  # crear nueva columna de duracion con solo valores numericos, (' .str.extract(r'(\d+)') '   ayuda a separar los numeros del texto) 
df_ml = df_ml.drop('duration', axis=1)
print(df_ml['duration_num'].isnull().sum()) #verificar que no haya alguna celda sin valor en la nueva columna 


#1.2 realizar One-Hot Encoding. 
df_encoded = pd.get_dummies(df_ml, columns= ['category', 'rating', 'type','duration_type'], drop_first=True) # usar .get_dummies para categorizar en binario cada columna puesta por cada valor de la columna 


#2. Escalar los datos
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_encoded) #se aplica el escalado
df_scaled = pd.DataFrame(df_scaled, columns= df_encoded.columns) #Convertimos de nuevo a DataFrame para conservar los nombres de columnas
print(df_scaled.head())

print(df_scaled.isnull().sum())
df_scaled = df_scaled.dropna()
#3. utilizar metodo del codo para verificar cuantos clusters se necesitan para esta practica
#3.1 incercia = Lista para guardar la inercia de cada K
inercia = []       #La inercia mide qué tan bien están agrupados los datos dentro de cada cluster.  Mientras más baja sea la inercia, mejor es la compactación de los puntos.


#3.2 Probar valores de K del 1 al 10
for k in  range(1,11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_scaled)
    inercia.append(kmeans.inertia_)


#3.3 graficar
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inercia, marker='o')
plt.title('Método del Codo (Elbow Method)')
plt.xlabel('Número de clusters (K)')
plt.ylabel('Inercia')
plt.grid(True)
plt.show()

print(df_ml['duration_num'].sort_values(ascending=False).head(10))
print(df_ml['release_year'].sort_values().head(10))

#4. Elegir K optimo 
kmeans = KMeans(n_clusters=3, random_state=42)# 1. Definir el modelo con el número óptimo de clusters
kmeans.fit(df_scaled)   # 2. Entrenar el modelo con tus datos escalados
df_scaled['cluster'] = kmeans.labels_   # 3. Obtener a qué cluster pertenece cada punto
df_result = pd.concat([df_ml.reset_index(drop=True), df_scaled['cluster']],axis=1)  # 4. unir la columna 'cluster' con el DataFrame original para analizar mejor

print('\n','Resumen de clusters','\n')
print(df_result['cluster'].value_counts())# 5. Ver un resumen de cuántos elementos hay en cada cluster
print(df_result.head())



