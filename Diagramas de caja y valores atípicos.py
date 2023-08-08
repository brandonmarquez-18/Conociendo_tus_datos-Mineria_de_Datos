import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leer el archivo CSV
data = pd.read_csv('glass.csv')

# Seleccionar los atributos para el cálculo
atributos = data.columns[:-1]  # Excluir la última columna 'Type of glass'

# Calcular el número de subplots necesarios
num_atributos = len(atributos)
num_filas = (num_atributos // 4) + 1

# Crear los diagramas de caja y detectar valores atípicos
plt.figure(figsize=(12, 8))
for i, atributo in enumerate(atributos):
    plt.subplot(num_filas, 4, i+1)
    sns.boxplot(x=data[atributo])
    plt.title(atributo)

plt.tight_layout()
plt.show()
