import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Leer el archivo CSV
data = pd.read_csv('glass.csv')

# Seleccionar los atributos para el cálculo
atributos = data.columns[:-1]  # Excluir la última columna 'Type of glass'

# Calcular la matriz de correlación
correlation_matrix = data[atributos].corr()

# Calcular la matriz de covarianza
covariance_matrix = data[atributos].cov()

print("Matriz de correlación:")
print(correlation_matrix)
print("\nMatriz de covarianza:")
print(covariance_matrix)


# Seleccionar los atributos para el cálculo
atributos = data.columns[:-1]  # Excluir la última columna 'Type of glass'

# Calcular la matriz de correlación
correlation_matrix = data[atributos].corr()

# Crear un mapa de calor de la matriz de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True,
            cmap='coolwarm', fmt=".2f", square=True)
plt.title('Matriz de Correlación')
plt.show()
