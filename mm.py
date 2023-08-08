import matplotlib.pyplot as plt
import pandas as pd
from statistics import mode

# Cargar la base de datos desde el archivo CSV
data = pd.read_csv('glass.csv')

# Calcular la media de cada atributo
media = data.mean()

# Calcular la mediana de cada atributo
mediana = data.median()

# Calcular la moda de cada atributo
moda = data.mode().iloc[0]

# Imprimir los resultados
print("Media:")
print(media)
print("\nMediana:")
print(mediana)
print("\nModa:")
print(moda)



# Calcular la media, mediana y moda para cada atributo
atributos = data.columns[:-1]  # Excluir la última columna 'Type of glass'
resultados = {}

for atributo in atributos:
    media = data[atributo].mean()
    mediana = data[atributo].median()
    moda = data[atributo].mode()[0]
    resultados[atributo] = {'Media': media, 'Mediana': mediana, 'Moda': moda}

# Crear gráfica para cada atributo
fig, axes = plt.subplots(nrows=len(atributos), figsize=(8, 6 * len(atributos)))

for i, atributo in enumerate(atributos):
    ax = axes[i]
    valores = data[atributo]
    ax.hist(valores, bins=20, edgecolor='black')
    ax.axvline(resultados[atributo]['Media'],
               color='r', linestyle='--', label='Media')
    ax.axvline(resultados[atributo]['Mediana'],
               color='g', linestyle='--', label='Mediana')
    ax.axvline(resultados[atributo]['Moda'],
               color='b', linestyle='--', label='Moda')
    ax.set_title(atributo)
    ax.legend()

plt.tight_layout()
plt.show()
