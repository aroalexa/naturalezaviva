def preguntarEdad():
    edad = int(input("Ingrese su edad: "))
    if edad>=18 and edad<60:
        print("Es mayor de edad")
    elif edad>70:
        print("Mayor que 70 anos")
    else:
        print("Los demas casos")

print("VAMOS A PREGUNTAR SU EDAD")
preguntarEdad()

# Uso de Break
for i in range(10):
    if i == 5:
        break
    print(i)
    # Uso de Continue
for i in range(5):
    if i == 2:
        continue
    print(i)