import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Leer el archivo CSV
data = pd.read_csv('glass.csv')

# Seleccionar los atributos para el cálculo de los componentes principales
atributos = data.columns[:-1]  # Excluir la última columna 'Type of glass'
X = data[atributos]

# Realizar el PCA
pca = PCA()
pca.fit(X)

# Obtener la varianza explicada por cada componente principal
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









# Seleccionar el número de componentes principales deseados (por ejemplo, 2)
num_componentes = 2

# Realizar la proyección de los datos originales en los componentes principales seleccionados
componentes_principales = pca.transform(X)[:, :num_componentes]

# Crear un DataFrame con las nuevas dimensiones
df_componentes = pd.DataFrame(componentes_principales, columns=[f'Componente {i+1}' for i in range(num_componentes)])

# Graficar la distribución de las nuevas dimensiones
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Componente 1', y='Componente 2', data=df_componentes)
plt.xlabel('Componente 1')
plt.ylabel('Componente 2')
plt.title('Distribución de las Nuevas Dimensiones')
plt.show()
