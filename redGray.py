import cv2
import numpy as np
import imutils

rojoBajo1 = np.array([0,140,90], np.uint8)
rojoAlto1 = np.array([8,255,255], np.uint8)
rojoBajo2 = np.array([160,140,90], np.uint8)
rojoAlto2 = np.array([180,255,255], np.uint8)

imagen = cv2.imread('img.jpeg')
imagen = imutils.resize(imagen, width=640)

imagenGris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
imagenGris = cv2.cvtColor(imagenGris, cv2.COLOR_GRAY2BGR)
imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

