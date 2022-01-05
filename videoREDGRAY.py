import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)

rojoBajo1 = np.array([0, 140, 90], np.uint8)
rojoAlto1 = np.array([8, 255, 255], np.uint8)
rojoBajo2 = np.array([160, 140, 90], np.uint8)
rojoAlto2 = np.array([180, 255, 255], np.uint8)

while True:
    ret,frame = cap.read()
    if ret == False: 
            break
    frame = imutils.resize(frame, width=640)

#convertimos los frames del video de bgr a gray

    frameGris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameGris = cv2.cvtColor(frameGris, cv2.COLOR_GRAY2BGR)
    frameHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

#detectamos el color rojo a cada uno de los frames 
    
    maskRojo1 = cv2.inRange(frameHSV, rojoBajo1,rojoAlto1)
    maskRojo2 = cv2.inRange(frameHSV, rojoBajo2,rojoAlto2)
    mask = cv2.add(maskRojo1,maskRojo2)
    mask = cv2.medianBlur(mask, 7)
    RojoDetected = cv2.bitwise_and(frame,frame, mask=mask)

#color de fondo gris 

    maskInv = cv2.bitwise_not(mask)
    bgGris = cv2.bitwise_and(frameGris,frameGris,mask=maskInv)

#se hace la suma de las imagenes para poder dar el efecto

    frameFinal = cv2.add(RojoDetected,bgGris)

#visualizar 
    cv2.imshow('FRAME DE PRUEBA', frame)
    cv2.imshow('FRAME FINAL', frameFinal)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()



