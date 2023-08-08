import pandas as pd
# Leer el archivo CSV
data = pd.read_csv('glass.csv')
# Definir umbrales para cada atributo basados en el análisis estadístico
umbrales = {
    'RI': 1.515,
    'Na': 14,
    'Mg': 3.5,
    'Al': 2.5,
    'Si': 73,
    'K': 5,
    'Ca': 10,
    'Ba': 1,
    'Fe': 0.15
}
# Clasificar los patrones según las reglas IF-THEN-ELSE
clases = []
for i, row in data.iterrows():
    clase = None
    if row['RI'] < umbrales['RI']:
        clase = 'Clase 1'
    elif row['Na'] > umbrales['Na'] and row['Mg'] < umbrales['Mg']:
        clase = 'Clase 2'
    elif row['Al'] > umbrales['Al'] and row['Si'] > umbrales['Si']:
        clase = 'Clase 3'
    elif row['K'] > umbrales['K'] and row['Ca'] > umbrales['Ca']:
        clase = 'Clase 4'
    elif row['Ba'] > umbrales['Ba'] or row['Fe'] > umbrales['Fe']:
        clase = 'Clase 5'
    else:
        clase = 'Clase 6'
    clases.append(clase)
# Agregar la columna 'Clase' al DataFrame original
data['Clase'] = clases
# Mostrar los resultados
print(data[['Id number', 'Clase']])
