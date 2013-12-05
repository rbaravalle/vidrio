"""
:Algoritmo para detectar piedras en vidrio
:version: 1.0
:author: Rodrigo Baravalle
:date: Diciembre 2013
:file: thresholding.py
:description: este algoritmo utiliza una tecnica de umbralado simple para segmentar las piedras por su transparencia
"""

from time import time
import Image
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from scipy import ndimage
import scipy
import csv
import white

t = time()

def fn(f,y):
    if(y == f): return 0
    return y


# segmentation algorithm
def segmentAlg(I,frame):
    n = 10
    np.random.seed(1)

    Nx, Ny = I.size

    im = np.asarray(I)

    mask = (im > im.mean()).astype(np.float)
    mask += 1 * im


    # Thresholding algorithm
    #binary_img = white.white(I,Nx,Ny,20,1.15)#mask < 80
    binary_img = im > 100
    #scipy.misc.imsave('images/outfile'+str(frame)+'_m.jpg', binary_img)

    binary_img = ndimage.binary_opening(binary_img, structure=np.ones((2,2))).astype(np.int)
    #scipy.misc.imsave('images/outfile'+str(frame)+'_m2.jpg', binary_img)

    label_im, nb_labels = ndimage.label(binary_img)

    sizes = ndimage.sum(mask, label_im, range(nb_labels + 1))
    mask_size = sizes > 150000
    remove_pixel = mask_size[label_im]
    label_im[remove_pixel] = 0

    #scipy.misc.imsave('images/outfile'+str(frame)+'_m3.jpg', label_im)

    return binary_img, label_im, nb_labels, sizes



# nsize: new size for image processing
def segment(I,frame,nsize):
    a,b = I.size
    r = np.float32(a)/b

    # Image size
    Nx = nsize
    Ny = int(nsize/r)

    I = I.resize((Nx,Ny), Image.ANTIALIAS) # best down-sizing filter

    I = I.convert('L') # rgb 2 gray

    # Segment current frame
    binary_img, label_im, nb_labels, sizes = segmentAlg(I,frame)
    

    coords = np.zeros((len(sizes)-1,2)).astype(np.float32)

    # Compute center of mass of segmented objects
    centers = ndimage.measurements.center_of_mass(label_im*2, label_im, range(len(sizes)))
  

    # Eliminate NANs in array
    centers = filter(lambda i: not(np.isnan(i[0])) and not(np.isnan(i[1])), centers)

    # Debug - Put Center of mass in Image
    for i in range(len(centers)):
        label_im[centers[i][0]][centers[i][1]] = 0

    # Save Image
    scipy.misc.imsave('images/outfile'+str(frame)+'.jpg', label_im*255)

    return centers


