import cv2
cap = cv2.VideoCapture(0)
majinBooClassif = cv2.CascadeClassifier('cascada.xml')
while True:
    
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    toy = majinBooClassif.detectMultiScale(gray,
    scaleFactor = 7,
    minNeighbors = 100,
    minSize=(90,100))
    for (x,y,w,h) in toy:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,'Quilmes',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()

""" Este código hace lo siguiente:

Importa el módulo cv2 para procesamiento de imágenes.
Inicia la captura de video desde la cámara.
Carga un clasificador de cascada previamente entrenado desde el archivo 'cascada.xml'.
Entra en un bucle que lee continuamente fotogramas de la cámara.
Convierte el fotograma a escala de grises.
Utiliza el clasificador de cascada para detectar objetos en escala de grises, en este caso, busca la apariencia de "Majin Boo".
Dibuja un rectángulo alrededor de las zonas detectadas como y agrega un texto identificativo.
Muestra el fotograma con las detecciones.
Espera a que se presione la tecla 'Esc' (código 27) para salir del bucle y liberar la captura de video """

