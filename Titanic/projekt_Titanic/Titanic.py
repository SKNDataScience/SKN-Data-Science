import csv
import numpy as np
lables=[]
with open('train.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    lables=next(csv_reader)


    matrix= [[]for i in range(0,891)]
    for i in range(891):
        matrix[i][:]=next(csv_reader)
# korelacje[]
# for i in range(12):
#     korelacje[i]=korelacja(i)
#
# def korelacja(a):
#     x = matrix[a][:]
#     pearsonr(x,matrix[1][:])
def srednia_wieku(matrix):
    suma = 0
    licz=0
    for i in range(891):
        try:
            suma += int(matrix[i][5])
            licz+=1

        except:
            continue
    return(suma/licz)



