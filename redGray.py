import cv2
import numpy as np
import imutils

#se crean los rangos para la deteccion de color
rojoBajo1 = np.array([0,140,90], np.uint8)
rojoAlto1 = np.array([8,255,255], np.uint8)
rojoBajo2 = np.array([160,140,90], np.uint8)
rojoAlto2 = np.array([180,255,255], np.uint8)

#se lee la imagen a tratar y se ajustan los tamaños
imagen = cv2.imread('img.jpeg')
imagen = imutils.resize(imagen, width=640)

#se transforma la imagen original en los distintos formatos a tratar
imagenGris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
imagenGris = cv2.cvtColor(imagenGris, cv2.COLOR_GRAY2BGR)
imagenHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

#detectamos el color rojo con los rangos especificos
maskRojo1 = cv2.inRange(imagenHSV,rojoBajo1,rojoAlto1)
maskRojo2 = cv2.inRange(imagenHSV,rojoBajo2,rojoAlto2)
mask = cv2.add(maskRojo1,maskRojo2)
mask = cv2.medianBlur(mask, 7)

rojoDetect = cv2.bitwise_and(imagen, imagen, mask=mask)

#fondo en color gris
maskInv = cv2.bitwise_not(mask)
bgGris = cv2.bitwise_and(imagenGris, imagenGris, mask=maskInv)

#se suman las imagenes rojodetect y bggris para obtener la imagen final
imagenFinal = cv2.add(rojoDetect,bgGris)

#se visualiza la imagen final
cv2.imshow('Resultado',imagenFinal)
cv2.imshow('IMAGEN DE ENTRADA', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()