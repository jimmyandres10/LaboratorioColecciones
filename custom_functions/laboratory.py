import numpy as np
import random
import array


a = np.zeros((3, 12))

for i in range(len(a)):

    for j in range(len(a[i])):

        if(i == 0):

            dep = "Santander"

        elif(i == 1):

            dep = "Guajira"

        else:

            dep = "Nariño"

        a[i][j] = (random.randrange(15, 31))

primerafila = a[[0, ], :]
segundafila = a[[1, ], :]
tercerafila = a[[2, ], :]
print(" santander: ", primerafila)
print(" Guajira: ", segundafila)
print(" Nariño: ", tercerafila)


tempSan = 0

tempGua = 0

tempNar = 0


for i in range(3):

    for j in range(12):

        if(i == 0):

            tempSan += a[i][j]

        if(i == 1):

            tempGua += a[i][j]

        else:

            tempNar += a[i][j]


promSan = tempSan/12

promGua = tempGua/12

promNar = tempNar/12

promNac = (promSan+promGua+promNar)/3

print(f"Promedio de la temperatura de santander {promSan}""\n",

      f"Promedio de la temperatura de Guajira {promGua}""\n",

      f"Promedio de la temperatura de Nariño {promNar}""\n",

      f"Promedio de la temperratura Nacional {promNac}""\n")


maxtemp1 = (np.max(primerafila))
maxtemp2 = (np.max(segundafila))
maxtemp3 = (np.max(tercerafila))
print(" la temperatura mayor en Santander: ", (np.max(primerafila)))
print(" la temperatura mayor en Guajira: ", (np.max(segundafila)))
print(" la temperatura mayor en Nariño: ", (np.max(tercerafila)))


b = int(input("digite la cantidad de meses en los que la temperatura fue maxima en Santander: "))
maxsb = maxtemp1*b
print(f"total de la suma de los meses en los que la temperatura fue maxima en Santander: {maxsb}")

c = int(input("digite la cantidad de meses en los que la temperatura fue maxima en la Guajira: "))
maxgc = maxtemp2*c
print(f"total de la suma de los meses en los que la temperatura fue maxima en la Guajira: {maxgc}")

d = int(input("digite la cantidad de meses en los que la temperatura fue maxima en Nariño: "))
maxnd = maxtemp3*d
print(f"total de la suma de los meses en los que la temperatura fue maxima en Nariño {maxnd}")


temp_max_prom = (maxsb+maxgc+maxnd)/3
print(
    f"promedio de los meses mas calientes de los 3 departamentos: {temp_max_prom}")


if(maxsb > maxgc and maxsb > maxnd):
    print(f"El promedio mayor es el de Santander {maxsb}")
elif(maxsb == maxgc and maxsb == maxnd):
    print("todos tienen el mismo promedio ")
elif(maxgc > maxsb and maxgc > maxnd):
    print(f"El promedio mayor es el de la Guajira {maxgc}")
elif(maxsb == maxgc):
    print("Santander y Guajira tienen los promedios mas altos ")
elif(maxnd > maxsb and maxnd > maxgc):
    print(f"El promedio mayor es el de Nariño {maxnd}")
elif(maxsb == maxnd):
    print("Santander y Nariño tienen los promedios mas altos")
elif(maxgc == maxnd):
    print("Guajira y Nariño tienen los promedios mas altos")
