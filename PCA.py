import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns


# Leer el archivo CSV
data = pd.read_csv('glass.csv')

# Seleccionar los atributos para el cálculo de los componentes principales
atributos = data.columns[:-1]  # Excluir la última columna 'Type of glass'
X = data[atributos]

# Calcular los componentes principales y la varianza explicada
pca = PCA()
componentes_principales = pca.fit_transform(X)
varianza_explicada = pca.explained_variance_ratio_

# Calcular la varianza acumulada
varianza_acumulada = np.cumsum(varianza_explicada)

# Graficar la varianza explicada y la varianza acumulada
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(varianza_explicada) + 1), varianza_explicada, marker='o', linestyle='-', label='Varianza Explicada')
plt.plot(range(1, len(varianza_acumulada) + 1), varianza_acumulada, marker='o', linestyle='-', label='Varianza Acumulada')
plt.xlabel('Número de Componentes Principales')
plt.ylabel('Varianza')
plt.title('Varianza Explicada y Varianza Acumulada')
plt.legend()
plt.show()

# Seleccionar el número de componentes principales que conservan la mayor parte de la información original
umbral_varianza = 0.95  # Por ejemplo, conservar el 95% de la varianza original
num_componentes = np.argmax(varianza_acumulada >= umbral_varianza) + 1

# Realizar la proyección de los datos originales en los componentes principales seleccionados
componentes_principales_seleccionados = componentes_principales[:, :num_componentes]

# Crear un DataFrame con las nuevas dimensiones
columnas_componentes = [f'Componente {i+1}' for i in range(num_componentes)]
df_componentes = pd.DataFrame(data=componentes_principales_seleccionados, columns=columnas_componentes)

# Graficar la distribución de las nuevas dimensiones
plt.figure(figsize=(8, 6))
for i in range(num_componentes):
    sns.histplot(data=df_componentes, x=f'Componente {i+1}', kde=True, label=f'Componente {i+1}')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Distribución de las Nuevas Dimensiones')
plt.legend()
plt.show()
