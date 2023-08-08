"""

import csv
import pandas as pd
import numpy as np

df=pd.read_csv("glass.csv", usecols=[3])
df2=pd.read_csv("glass.csv",usecols=[4])

data=df.to_numpy()
etiquetas_clase=df2.to_numpy()

def Clasificador_IF_THEN(x):
    clase=[]
    for i in range(len(x)):
        if x[i] < 0.75:
            clase.append("1")
        if x[i] >= 0.75 and x[i] < 1.7:
            clase.append("2")
        if x[i] >= 1.7:
            clase.append("3")
    return clase
    

prediccion_clases=Clasificador_IF_THEN(data)

from operator import eq

rendimiento=sum(map(eq,etiquetas_clase,prediccion_clases))

print("Rendimiento del clasificador", rendimiento/len(data) * 100, "%")


"""


import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Cargar los datos desde el archivo CSV
data = np.genfromtxt('glass.csv', delimiter=',', skip_header=1, usecols=(-2, -1))

# Separar las características (X) y las etiquetas (y)
X = data[:, :-1]
y = data[:, -1]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el clasificador Naive Bayes
clf = GaussianNB()

# Entrenar el clasificador
clf.fit(X_train, y_train)

# Realizar predicciones sobre los datos de prueba
y_pred = clf.predict(X_test)

# Calcular el rendimiento del clasificador
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
