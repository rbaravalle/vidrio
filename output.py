"""
:Algoritmo para detectar piedras en vidrio
:version: 1.0
:author: Rodrigo Baravalle
:date: Diciembre 2013
:file: output.py
:description: devuelve la salida del algoritmo y la imprime
"""

import numpy as np
import csv


# Save points in a csv file
def saveData(points,frame):
    filec = 'csv/coords'+str(frame)+'.csv'
    with open(filec, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(np.array(points).astype(np.int))
