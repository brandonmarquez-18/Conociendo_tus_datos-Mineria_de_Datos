import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Leer el archivo CSV
data = pd.read_csv('glass.csv')

# Calcular el rango, cuartiles, varianza, desviación estándar y rango intercuartílico para cada atributo
atributos = data.columns[:-1]  # Excluir la última columna 'Type of glass'
resultados = {}

for atributo in atributos:
    valores = data[atributo]
    rango = valores.max() - valores.min()
    cuartiles = valores.quantile([0.25, 0.5, 0.75])
    varianza = valores.var()
    desviacion_estandar = valores.std()
    rango_intercuartilico = cuartiles[0.75] - cuartiles[0.25]

    resultados[atributo] = {
        'Rango': rango,
        'Cuartiles': cuartiles,
        'Varianza': varianza,
        'Desviación Estándar': desviacion_estandar,
        'Rango Intercuartílico': rango_intercuartilico
    }

# Imprimir los resultados
for atributo, estadisticos in resultados.items():
    print(f"Atributo: {atributo}")
    print(f"Rango: {estadisticos['Rango']}")
    print(f"Cuartiles: {estadisticos['Cuartiles']}")
    print(f"Varianza: {estadisticos['Varianza']}")
    print(f"Desviación Estándar: {estadisticos['Desviación Estándar']}")
    print(f"Rango Intercuartílico: {estadisticos['Rango Intercuartílico']}")
    print()


# Generar los boxplots para cada atributo
atributos = data.columns[:-1]  # Excluir la última columna 'Type of glass'

for atributo in atributos:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=atributo, data=data)
    plt.title(f'Boxplot de {atributo}')
    plt.show()
