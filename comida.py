import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv("indian_food.csv")

datos = datos.drop(["name", "ingredients"], axis=1)
print(datos.shape)

sizes = [
    datos[datos["flavor_profile"]==datos["flavor_profile"].unique()[0]].shape[0], 
    datos[datos["flavor_profile"]==datos["flavor_profile"].unique()[1]].shape[0], 
    datos[datos["flavor_profile"]==datos["flavor_profile"].unique()[2]].shape[0], 
    datos[datos["flavor_profile"]==datos["flavor_profile"].unique()[3]].shape[0], 
    datos[datos["flavor_profile"]==datos["flavor_profile"].unique()[4]].shape[0]
    ]

labels = [
    datos["flavor_profile"].unique()[0], 
    datos["flavor_profile"].unique()[1], 
    datos["flavor_profile"].unique()[2], 
    datos["flavor_profile"].unique()[3], 
    datos["flavor_profile"].unique()[4]
    ]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()

sizes = [
    datos[datos["diet"]=="vegetarian"].shape[0], 
    datos[datos["diet"]=="non vegetarian"].shape[0]
    ]
labels = [
    datos["diet"].unique()[0], 
    datos["diet"].unique()[1]
    ]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()

sizes = [
    datos[datos["course"]==datos["course"].unique()[0]].shape[0], 
    datos[datos["course"]==datos["course"].unique()[1]].shape[0], 
    datos[datos["course"]==datos["course"].unique()[2]].shape[0], 
    datos[datos["course"]==datos["course"].unique()[3]].shape[0]
    ]

labels = [
    datos["course"].unique()[0], 
    datos["course"].unique()[1], 
    datos["course"].unique()[2], 
    datos["course"].unique()[3]
    ]
plt.bar(labels, sizes)
plt.show()

sizes = [
    datos[datos["region"]==datos["region"].unique()[0]].shape[0], 
    datos[datos["region"]==datos["region"].unique()[1]].shape[0], 
    datos[datos["region"]==datos["region"].unique()[2]].shape[0], 
    datos[datos["region"]==datos["region"].unique()[3]].shape[0],
    datos[datos["region"]==datos["region"].unique()[4]].shape[0],
    datos[datos["region"]==datos["region"].unique()[5]].shape[0],
    datos[datos["region"]==datos["region"].unique()[6]].shape[0],
    datos[datos["region"]==datos["region"].unique()[7]].shape[0],
    ]

labels = [
    datos["region"].unique()[0], 
    datos["region"].unique()[1], 
    datos["region"].unique()[2], 
    datos["region"].unique()[3],
    datos["region"].unique()[4],
    datos["region"].unique()[5],
    datos["region"].unique()[6],
    datos["region"].unique()[7],
    ]
plt.pie(sizes, labels=labels)
plt.show()

x = np.arange(datos["prep_time"].shape[0])
y1 = datos["prep_time"]
plt.plot(x, y1)
plt.show()

y2 = datos["cook_time"]
plt.scatter(y1, y2, s=4)
plt.xlabel("prep_time")
plt.ylabel("cook_time")
plt.show()