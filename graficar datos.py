import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("glass.csv")
data.hist(figsize=(10, 8))
plt.tight_layout()
plt.show()




data = pd.read_csv("glass.csv")
data.boxplot(figsize=(10, 8))
plt.tight_layout()
plt.show()



data = pd.read_csv("glass.csv")
plt.figure(figsize=(10, 8))
plt.scatter(data['RI'], data['Na'], c=data['Type of glass'])
plt.xlabel('RI')
plt.ylabel('Na')
plt.title('Distribución de RI vs. Na')
plt.colorbar(label='Tipo de vidrio')
plt.show()
