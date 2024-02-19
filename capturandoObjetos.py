import cv2
import numpy as np
import imutils
import os

Datos = 'n'
if not os.path.exists(Datos):
	print('Carpeta creada: ', Datos)
	os.makedirs(Datos)

cap = cv2.VideoCapture(0)

x1, y1 = 190, 80
x2, y2 = 450, 398

count = 0
while True:

	ret, frame = cap.read()
	if ret == False:  break
	imAux = frame.copy()
	cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

	objeto = imAux[y1:y2,x1:x2]
	objeto = imutils.resize(objeto, width=38)
	# print(objeto.shape)

	k = cv2.waitKey(1)
	if k == ord('s'):
		cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),objeto)
		print('Imagen almacenada: ', 'objeto_{}.jpg'.format(count))
		count = count + 1
	if k == 27: 
		break

	cv2.imshow('frame',frame)
	cv2.imshow('objeto',objeto)

cap.release()
cv2.destroyAllWindows()



""" Este código realiza lo siguiente:

Importa los módulos necesarios: cv2 (OpenCV), numpy, imutils y os.
Crea una carpeta llamada 'n' si no existe.
Inicia la captura de video desde la cámara (dispositivo 0).
Define las coordenadas de un rectángulo en el marco de la imagen.
Entra en un bucle que lee continuamente fotogramas de la cámara.
Dentro del bucle, muestra el fotograma actual y un recorte del área delimitada por el rectángulo.
Permite al usuario presionar la tecla 's' para capturar y almacenar una imagen del objeto dentro del rectángulo.
Muestra el objeto recortado en una ventana aparte.
Si el usuario presiona la tecla 'Esc', se sale del bucle y se libera la captura de video.

En resumen, este código permite capturar imágenes de un objeto delimitado por un rectángulo en tiempo real desde una cámara,
 almacenándolas en una carpeta designada cuando se presiona la tecla 's'. """