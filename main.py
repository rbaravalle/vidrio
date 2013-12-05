"""
:Algoritmo para detectar piedras en vidrio
:version: 1.0
:author: Rodrigo Baravalle
:date: Diciembre 2013
:file: main.py
:description: archivo principal
"""
import cv2
import sys
import numpy as np
import time
import Image
import errno
import os
import scipy
import output

# Segmentation algorithms
import thresholding
import plotLabel
from parameters import *

# Algorithms array
algorithms = [thresholding,plotLabel]

# Video Capture
cap = cv2.VideoCapture(video)
cv2.namedWindow("input")

# Create path and raise any error
def create_path(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

# Create paths to store data
def create_paths():
    directory = ['csv','images']
    for i in range(len(directory)):
        if not os.path.exists(directory[i]):
            create_path(directory[i])

def main():
    # Create paths  
    create_paths()

    videoFrame = 0
    frames = 0
    last_time = time.time()

    while(True):
        # Obtain actual frame from video
        success, img = cap.read()
        # Save Image
        #scipy.misc.imsave('images/outfile'+str(videoFrame)+'_f.jpg', img)

           
        if(videoFrame > -1): 
            if(success):
                #cv2.imshow("input", img)

                # Image processing
                img = Image.fromarray(img,'RGB')
                centers = algorithms[actual_algorithm].segment(img,videoFrame,nsize)

                # Save output
                output.saveData(centers,videoFrame)

                cv2.waitKey(1)
                
                # Debug - FPS (Frames Per Second)
                frames += 1
                if time.time() - last_time >= 1:
                    current_fps = frames / (time.time() - last_time)
                    print current_fps, ' fps'
                    frames = 0
                    last_time = time.time()

            else: 
                #print "Warning. Frame: " + str(videoFrame) + " not processed, at time: " + str(time.time())
                print "Last Frame: " + str(videoFrame)
                return

        videoFrame+=1

def testImage(filename):
    img = Image.open(filename)
    #img = Image.fromarray(img,'RGB')
    algorithms[actual_algorithm].segment(img,-1,nsize)
    

#Begin loop
main()
#testImage('data/test2.jpg')
