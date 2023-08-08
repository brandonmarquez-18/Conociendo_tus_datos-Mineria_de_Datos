from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

sns.set()
df = pd.read_csv('glass.csv')

# Informacion de los datos
df.info()

df.describe()

print(df[df.duplicated()])

print(df["Type of glass"].value_counts())

plt.title('Elementos por clase')
# Informacion estadistica por atributo
df.describe(include = 'all')

# Valores duplicados
print(df[df.duplicated()] , "medidas de tencia central")

# Valores count
print(df["Type of glass"].value_counts(), "valores countttt")

# Na
print(df["Na"].value_counts())

#
plt.title('Elementos por clase distribucion')
print(sns.countplot(x=df["Type of glass"]))
#Gráficos de dispersión:
sns.scatterplot(x = df["Id number"], y = df["RI"], hue = df["Type of glass"])
sns.scatterplot(x = df["Id number"], y = df["Na"], hue = df["Type of glass"])
sns.scatterplot(x = df["Id number"], y = df["Mg"], hue = df["Type of glass"])
sns.scatterplot(x = df["Id number"], y = df["Al"], hue = df["Type of glass"])
sns.scatterplot(x = df["Id number"], y = df["Si"], hue = df["Type of glass"])
sns.scatterplot(x = df["Id number"], y = df["K"], hue = df["Type of glass"])
sns.scatterplot(x = df["Id number"], y = df["Ca"], hue = df["Type of glass"])
sns.scatterplot(x = df["Id number"], y = df["Ba"], hue = df["Type of glass"])
sns.scatterplot(x = df["Id number"], y = df["Fe"], hue = df["Type of glass"])

# Tarea con if separar clases

#Pairplot
sns.pairplot(df, hue = "Type of glass")

# plt.figure()
#Matriz de correlacion
sns.heatmap(df.corr(), annot=True)

print(df.groupby("Type of glass").agg((["mean", "median"])))

plt.show()

#box plot
fig, axes = plt.subplots(4, 3, figsize=(16, 9))
sns.boxplot(y="Id number", x="Type of glass", data=df, orient="v", ax=axes[0, 0])
sns.boxplot(y="RI", x="Type of glass", data=df, orient="v", ax=axes[0, 1])
sns.boxplot(y="Na", x="Type of glass", data=df, orient="v", ax=axes[0, 2])
sns.boxplot(y="Mg", x="Type of glass", data=df, orient="v", ax=axes[1, 0])
sns.boxplot(y="Al", x="Type of glass", data=df, orient="v", ax=axes[1, 1])
sns.boxplot(y="Si", x="Type of glass", data=df, orient="v", ax=axes[1, 2])
sns.boxplot(y="K", x="Type of glass", data=df, orient="v", ax=axes[2, 0])
sns.boxplot(y="Ca", x="Type of glass", data=df, orient="v", ax=axes[2, 1])
sns.boxplot(y="Ba", x="Type of glass", data=df, orient="v", ax=axes[2, 2])
sns.boxplot(y="Fe", x="Type of glass", data=df, orient="v", ax=axes[3, 0])



sns.FacetGrid(df, hue="Type of glass", height=5)\
    .map(sns.distplot, "Id number")\
    .add_legend()

sns.FacetGrid(df, hue="Type of glass", height=5)\
    .map(sns.distplot, "RI")\
    .add_legend()

sns.FacetGrid(df, hue="Type of glass", height=5)\
    .map(sns.distplot, "Na")\
    .add_legend()

sns.FacetGrid(df, hue="Type of glass", height=5)\
    .map(sns.distplot, "Mg")\
    .add_legend()

sns.FacetGrid(df, hue="Type of glass", height=5)\
    .map(sns.distplot, "Al")\
    .add_legend()

sns.FacetGrid(df, hue="Type of glass", height=5)\
    .map(sns.distplot, "Si")\
    .add_legend()

sns.FacetGrid(df, hue="Type of glass", height=5)\
    .map(sns.distplot, "K")\
    .add_legend()

sns.FacetGrid(df, hue="Type of glass", height=5)\
    .map(sns.distplot, "Ca")\
    .add_legend()

sns.FacetGrid(df, hue="Type of glass", height=5)\
    .map(sns.distplot, "Ba")\
    .add_legend()

sns.FacetGrid(df, hue="Type of glass", height=5)\
    .map(sns.distplot, "Fe")\
    .add_legend()



print(df.corr)
print(df.cov)

df
data = df.drop(["Type of glass"], axis=1)
print(data)

data_normal = StandardScaler().fit_transform(data)
print(data_normal)


df_normal = pd.DataFrame(data_normal, columns=[
                         "Id number","RI","Na","Mg","Al","Si","K","Ca","Ba","Fe"])
                    
print(data_normal)

df_normal["Type of glass"] = df["Type of glass"]
print(df_normal)


sns.pairplot(df_normal, hue="Type of glass")

print(df_normal.corr)

print(df_normal.cov)

df_normal["RI"].var()

fig, axes = plt.subplots(4, 3, figsize=(16, 9))

sns.boxplot(y="Id number", x="Type of glass",
            data=df_normal, orient="v", ax=axes[0, 0])
sns.boxplot(y="RI", x="Type of glass",
            data=df_normal, orient="v", ax=axes[0, 1])
sns.boxplot(y="Na", x="Type of glass",
            data=df_normal, orient="v", ax=axes[0, 2])
sns.boxplot(y="Mg", x="Type of glass",
            data=df_normal, orient="v", ax=axes[1, 0])
sns.boxplot(y="Al", x="Type of glass",
            data=df_normal, orient="v", ax=axes[1, 1])
sns.boxplot(y="Si", x="Type of glass",
            data=df_normal, orient="v", ax=axes[1, 2])
sns.boxplot(y="K", x="Type of glass",
            data=df_normal, orient="v", ax=axes[2, 0])
sns.boxplot(y="Ca", x="Type of glass",
            data=df_normal, orient="v", ax=axes[2, 1])
sns.boxplot(y="Ba", x="Type of glass",
            data=df_normal, orient="v", ax=axes[2, 2])
sns.boxplot(y="Fe", x="Type of glass",
            data=df_normal, orient="v", ax=axes[3, 0])




plt.show()

pca = PCA(n_components=3)
principalComponents = pca.fit_transform(data_normal)

pca.get_covariance()

df_normal.cov

principalComponents

principal_df = pd.DataFrame(principalComponents, columns=[
                            "PCA1", "PCA2", "PCA3"])
final_df = pd.concat([principal_df, df[["Type of glass"]]], axis=1)
print(final_df)




varianza = pca.explained_variance_ratio_


suma = varianza[0] + varianza[1]
print(varianza)

plt.figure(figsize=(3, 2))
plt.bar(range(3), varianza, alpha=0.5, align="center")
plt.ylabel("Varianza")
plt.xlabel("Principal components")
plt.show()


reducida_df = final_df.drop(["PCA3"], axis=1)
print(reducida_df)

sns.pairplot(reducida_df, hue="Type of glass", height=4)

label_encoder = LabelEncoder()
etiquetas = label_encoder.fit_transform(reducida_df["Type of glass"])
print(etiquetas)


data_training = reducida_df.drop(["Type of glass"], axis=1)
clf = MLPClassifier(solver="lbfgs", alpha=1e-5, hidden_layer_sizes=(1000, 200, 50, 50), random_state=1)

clf.fit(data_training, etiquetas)
puntuation = clf.score(data_training, etiquetas)

print(puntuation)










