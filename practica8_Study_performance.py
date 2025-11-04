import pandas as pd 
from pandas import get_dummies
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn. linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

#--------------------cargar y analisis de base de datos-----------------
df = pd.read_csv('practicas\data\study_performance.csv')
print(df.head(5))
df.info()
print('\n')
print(df.nunique())
print(df.columns)


#---------------------------Limpieza de Datos---------------------------

# 1. usar get_dummies para realizar One-Hot encoder en columnas categoricas
df = pd.get_dummies(df, columns=['gender', 'race_ethnicity', 'lunch', 'test_preparation_course'], dtype= int)

# 2. usar ordinal encoder para la columna "parental_level_of_education"
print(df['parental_level_of_education'].value_counts())
ordinal_categories = [['some high school', 'high school', 'some college', "associate's degree", "bachelor's degree", "master's degree"]]

ordinal_encoder = OrdinalEncoder(categories= ordinal_categories)
df['parental_level_of_education_encoded'] = ordinal_encoder.fit_transform(df[['parental_level_of_education']])
df.drop('parental_level_of_education', axis=1, inplace=True)

# 3. crear columna promedio y eliminar columnas "score"
df['score'] = round(df[['math_score','reading_score','writing_score']].mean(axis= 1)*.1,1)
df[['math_score', 'reading_score','writing_score']]= df[['math_score', 'reading_score','writing_score']]*.1
print(df)



#----------------------------Machine Learning----------------------------------

# 1. seleccionar "X" y "y" 
X = df.drop(['score','math_score', 'reading_score','writing_score'], axis=1)
y = df['score'] 

# 2. Hacer el modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape)
print(y_train.shape)

rf_model = RandomForestRegressor()
rf_model.fit (X_train, y_train)


lr_model = LinearRegression()
lr_model.fit (X_train, y_train)

# 3. Realizar predicciones
rf_predict = rf_model.predict(X_test)
lr_predict = lr_model.predict(X_test)

# 4. Calcular MSE para verificar que tanto se ha equivocado nuestro modelo
mse_rf = mean_squared_error(y_test, rf_predict)
r2_rf = r2_score(y_test, rf_predict)
mae_rf = mean_absolute_error(y_test, rf_predict)

mse_lr = mean_squared_error(y_test, lr_predict)
r2_lr = r2_score(y_test, lr_predict)
mae_lr = mean_absolute_error(y_test, lr_predict)

print('RANDOM FOREST MSE: ', mse_rf)
print('RANDOM FOREST R2: ', r2_rf)
print('RANDOM FOREST MAE: ', mae_rf)
print('\n')
print('LINEAR REGRESSION MSE: ',mse_lr)
print('LINEAR REGRESION R2: ', r2_lr)
print('LINEAR REGRESION MAE: ', mae_lr)

print('\n')
print(df.corr(numeric_only=True)['score'].sort_values(ascending=False))


# Visualización grafica 

plt.plot(y_test.values, color= 'green', label= 'Real', alpha= 0.6)
plt.plot(lr_predict, color= 'purple', label= 'Predicho (LR)', linestyle=':', alpha= 1)

plt.xlabel("Muestras")
plt.ylabel("Puntaje")
plt.title("Comparación Real vs Predicho - LR")
plt.legend()
plt.show()

