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

def segment(im,frame, nsize):
    a,b = im.size
    r = np.float32(a)/b

    l = nsize
    Nx = l
    Ny = int(l/r)
    im = im.resize((Nx,Ny), Image.ANTIALIAS) # best down-sizing filter
    image = im.convert('L') # rgb 2 gray
    image = np.asarray(image)

    # apply threshold
    thresh = threshold_otsu(image)
    bw = closing(image > thresh, square(3))

    # remove artifacts connected to image border
    cleared = bw.copy()
    clear_border(cleared)
    cleared = bw

    # label image regions
    label_image = label(cleared)
    borders = np.logical_xor(bw, cleared)
    label_image[borders] = -1
    image_label_overlay = label2rgb(label_image, image=image)

    fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
    ax.imshow(image_label_overlay)

    centers = []

    i = 0
    for region in regionprops(label_image, ['Area', 'BoundingBox']):

        if region['Area'] > 10000:
            continue

        # draw rectangle around segmented objects
        minr, minc, maxr, maxc = region['BoundingBox']
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill=False, edgecolor='red', linewidth=2)
        #print rect
        ax.add_patch(rect)
        x0 = int((maxc+minc)/2)
        y0 = int((maxc+minc)/2)
        if(not(x0 == 0 and y0 == 0)):
            centers.append([x0,y0])


    # Save "centers of mass" coordinates in a csv file
    filec = 'csv/coords'+str(frame)+'.csv'
    with open(filec, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(np.array(centers).astype(np.int))

    #scipy.misc.imsave('images/outfile'+str(frame)+'.jpg', ax)
    plt.savefig('images/outfile'+str(frame)+'.jpg')

