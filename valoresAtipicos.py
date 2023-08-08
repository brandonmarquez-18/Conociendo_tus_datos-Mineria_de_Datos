import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tabulate import tabulate

# Leer el archivo CSV
data = pd.read_csv('glass.csv')

# Seleccionar los atributos para el cálculo
atributos = data.columns[:-1]  # Excluir la última columna 'Type of glass'

# Calcular el número de subplots necesarios
num_atributos = len(atributos)
num_filas = (num_atributos // 4) + 1

# Crear los diagramas de caja y detectar valores atípicos
plt.figure(figsize=(12, 8))
outliers = {}  # Diccionario para almacenar los valores atípicos por atributo

for i, atributo in enumerate(atributos):
    plt.subplot(num_filas, 4, i+1)
    sns.boxplot(x=data[atributo])
    plt.title(atributo)
    
    # Detectar valores atípicos utilizando el rango intercuartílico (IQR)
    q1 = data[atributo].quantile(0.25)
    q3 = data[atributo].quantile(0.75)
    iqr = q3 - q1
    lower_threshold = q1 - 1.5 * iqr
    upper_threshold = q3 + 1.5 * iqr
    
    outliers[atributo] = data[(data[atributo] < lower_threshold) | (data[atributo] > upper_threshold)]

plt.tight_layout()
plt.show()

# Mostrar los registros considerados como valores atípicos por atributo
for atributo, df_outliers in outliers.items():
    print(f"Valores atípicos en el atributo '{atributo}':")
    
    # Marcar los registros atípicos en rojo
    df_outliers_styled = df_outliers.style.apply(lambda x: ['background-color: red']*len(x), axis=1)
    
    # Mostrar la tabla de valores atípicos
    print(df_outliers_styled.render())

    print()
