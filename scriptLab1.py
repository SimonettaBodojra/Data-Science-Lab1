import csv
import math
# se hai bisogno solo di alcune funzioni di una specifica libreria puoi decidere quale caricare singolarmente
from statistics import mean, stdev

with open("iris.csv") as irisData:  # apro il file, tipo fopen
    csvReader = csv.reader(irisData)  # creo il reader, il riferimento al file che devo leggere, lo scorrerò per righe
    listIris = []  # creo una lista dentro cui inserire gli elementi, non è una definizione di variabile
    for row in csvReader:  # row è la variabile d'appoggio che contiene la riga corrente ad ogni ciclo
        if len(row) != 0:
            listIris.append(list(row))  # non sappiamo cosa sia row, quindi si fa il cast a lista, e ogni lista va messa dentro l'irisList

total = len(listIris) # len calcola la lunghezza di qualsiasi cosa

sumSepalLength = .0 # metto .0 per far capire al pc stupido che parto da un floaaat
sumSepalWidth = .0
sumPetalLength = .0
sumPetalWidth = .0

for row in listIris:
    sumSepalLength += float(row[0]) # metto il cast perché gli elementi della row sono stringhe prelevate dal dataset
    sumSepalWidth += float(row[1])
    sumPetalLength += float(row[2])
    sumPetalWidth += float(row[3])

# calcolo le medie
meanSepalLength = sumPetalLength/total
meanSepalWidth = sumPetalWidth/total
meanPetalLength = sumPetalLength/total
meanPetalWidth = sumPetalWidth/total

sqSepalLength = .0
sqSepalWidth = .0
sqPetalLength = .0
sqPetalWidth = .0

for row in listIris:
    sqSepalLength += math.pow(float(row[0])-meanSepalLength, 2)
    sqSepalWidth += math.pow(float(row[1])-meanSepalWidth, 2)
    sqPetalLength += math.pow(float(row[2])-meanPetalLength, 2)
    sqPetalWidth += math.pow(float(row[3])-meanPetalWidth, 2)

#calcolo le varianze
sdSepalLength = math.sqrt(sqSepalLength/total)
sdSepalWidth = math.sqrt(sqSepalWidth/total)
sdPetalLength = math.sqrt(sqPetalLength/total)
sdPetalWidth = math.sqrt(sqPetalWidth/total)

print(f"Means: {meanSepalLength:.2f}, {meanSepalWidth:.2f}, {meanPetalLength:.2f}, {meanPetalWidth:.2f}")
print(f"Standard deviations: {sdSepalLength:.2f}, {sdSepalWidth:.2f}, {sqPetalLength:.2f}, {sqPetalWidth:.2f}")

#calcolo il punto tre

listVersicolor = []
listVirginica = []
listSetosa = []

for row in listIris:
    if "versicolor" in str(row[4]).lower():
        listVersicolor.append(row)
    elif "virginica" in str(row[4]).lower():
        listVirginica.append(row)
    elif "setosa" in str(row[4]).lower():
        listSetosa.append(row)

# Creo una tupla contenente le liste divise per categoria in modo tale da non ripetere tre volte lo stesso codice
groupedLists = (listVersicolor, listVirginica, listSetosa)

# groupedList conterrà al primo ciclo listVersicolor, al secondo listVirginica
for groupedList in groupedLists:
    sepalL = []
    sepalW = []
    petalL = []
    petalW = []


    for row in groupedList:
        sepalL.append(float(row[0]))
        sepalW.append(float(row[1]))
        petalL.append(float(row[2]))
        petalW.append(float(row[3]))

    category = ""
    if "versicolor" in str(groupedList[0][4]).lower():
        category = "Versicolor"
    elif "virginica" in str(groupedList[0][4]).lower():
        category = "Virginica"
    elif "setosa" in str(groupedList[0][4]).lower():
        category = "Setosa"

    print()
    print(f"{category} mean: {mean(sepalL):.2f}, {mean(sepalW):.2f}, {mean(petalL):.2f}, {mean(petalW):.2f}")
    print(f"{category} stdev: {stdev(sepalL):.2f}, {stdev(sepalW):.2f}, {stdev(petalL):.2f}, {stdev(petalW):.2f}")
