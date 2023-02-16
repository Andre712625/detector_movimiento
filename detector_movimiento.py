import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Iniciar la cámara
cap.set(3, 640)  # Ancho de la imagen
cap.set(4, 480)  # Alto de la imagen

while True:
    _, frame = cap.read()  # Capturar un fotograma
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convertir a espacio de color HSV

    # Definir rangos de color a detectar
    lower_color = np.array([0, 50, 50])
    upper_color = np.array([10, 255, 255])

    # Crear una máscara para el color
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Encontrar los contornos en la máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos en el fotograma original
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Mostrar el resultado
    cv2.imshow('frame', frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Liberar la cámara
cv2.destroyAllWindows()  # Cerrar todas las ventanas

