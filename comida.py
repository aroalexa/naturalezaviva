import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("indian_food.csv")

#print(datos.head())

#print(datos.describe())

#datos["diet"] = datos["diet"].replace("vegetarian",1)
#datos["diet"] = datos["diet"].replace("non vegetarian",0)

#print(datos[datos["diet"]=="vegetarian"].shape[0])

sizes = [datos[datos["diet"]=="vegetarian"].shape[0], datos[datos["diet"]=="non vegetarian"].shape[0]]
labels = [datos["diet"].unique()[0], datos["diet"].unique()[1]]
#print(datos[datos["diet"]=="vegetarian"].shape)
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()
