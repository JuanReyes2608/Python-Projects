import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# datos de ejemplo 
data = {
    'size': [50, 60, 80, 100 ,120],
    'price': [150000, 180000, 210000, 250000, 280000]
}
df = pd.DataFrame(data)


x = df[['size']] #variable independiente
y = df['price']  #variable dependiente

model = LinearRegression()
model.fit(x, y)


# predicción
predicion = model.predict ([[90]])
print(f'El precio de una casa de 90 m2 es: {predicion[0]:.2f}')

plt.scatter(x, y, color='blue')
plt.plot(x, model.predict(x), color='red') 
plt.xlabel('Tamaño (m2)')
plt.ylabel('Precio ($)')
plt.title('Precio de casas según tamaño')
plt.show()