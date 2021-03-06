"""
:Algoritmo para detectar piedras en vidrio
:version: 1.0
:author: Rodrigo Baravalle
:date: Diciembre 2013
:file: plotLabel.py
:description: algoritmo que utiliza umbralamiento de Otsu junto a closing binario
"""


"""
===================
Label image regions
===================

This example shows how to segment an image with image labelling. The following
steps are applied:

1. Thresholding with automatic Otsu method
2. Close small holes with binary closing
3. Remove artifacts touching image border
4. Measure image regions to filter small objects

"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage import data
from skimage.filter import threshold_otsu
from skimage.segmentation import clear_border
from skimage.morphology import label, closing, square
from skimage.measure import regionprops
from skimage.color import label2rgb
import Image
import scipy
import csv
from parameters import *

def segment(im,frame, nsize):
    a,b = im.size
    r = np.float32(a)/b

    l = nsize
    Nx = l
    Ny = int(l/r)
    im = im.resize((Nx,Ny))
    image = im.convert('L') # rgb 2 gray
    image = np.asarray(image)

    # apply threshold
    thresh = threshold_otsu(image)
    # thresh = image.mean()
    #bw = closing(image > thresh, square(3))
    bw = image < 1.2*thresh
    #fig, ax = plt.subplots(ncols=1, nrows=1)#, figsize=(6, 6))
    #ax.imshow(bw, cmap=matplotlib.cm.gray)

    # remove artifacts connected to image border
    #cleared = bw.copy()
    #clear_border(cleared)
    #cleared = bw

    # label image regions
    label_image = label(bw)
    #borders = np.logical_xor(bw, cleared)
    #label_image[borders] = -1
    #image_label_overlay = label_image#label2rgb(label_image, image=image)

    #fig, ax = plt.subplots(ncols=1, nrows=1)#, figsize=(6, 6))
    #ax.imshow(image_label_overlay)
    

    centers = []

    i = 0
    array = regionprops(label_image, ['Area', 'BoundingBox'])
    array = filter(lambda i: i['Area'] < maxArea and i['Area'] > minArea,array)
    centers = map(lambda i: i['centroid'],array)
    print len(centers)

    #plt.savefig('images/outfile'+str(frame)+'.jpg')

    return centers

