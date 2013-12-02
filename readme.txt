"""
:Algoritmo para detectar piedras en vidrio
:version: 1.0
:author: Rodrigo Baravalle
:date: Diciembre 2013
:file: readme.txt
:description: archivo con información de instalado y utilización
"""

El programa toma una entrada de video y produce una salida por frame con los elementos indeseados marcados en un archivo de texto

-------------------------
Requerimientos:
python 2.7
opencv 2.x

python packages:
bindings de python para opencv
Numpy 1.1 or higher (http://numpy.scipy.org/)
Scipy 0.7 or higher (http://www.scipy.org/)
PIL 1.1.7 or higher (http://www.pythonware.com/products/pil/)
scikit-image: (si se usa plotLabel, http://scikit-image.org/docs/0.9.x/install.html)
Cython 0.19 or higher (si se usa plotLabel, )

-------------------------
Funcionamiento:

ejecutar en una consola:

python main.py

main.py crea las carpetas "csv" y "images".

En la carpeta csv se guardan las coordenadas de los elementos indeseados en cada frame
En la carpeta images se puede ver en la imagen cada elemento indeseado marcado

-------------------------
Archivos:

main.py :         algoritmo principal, procesamiento del video, escritura de resultados
parameters.py:       parámetros del algoritmo
thresholding.py : algoritmo que usa un umbral para segmentar (simple y rapido)
label.py:         algoritmo que usa umbral de Otsu y closing (mas lento)

