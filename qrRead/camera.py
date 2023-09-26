import cv2
from pyzbar.pyzbar import decode
import pygame
import time

pygame.mixer.init()

cap = cv2.VideoCapture(0)

cv2.namedWindow("Kamera Görüntüsü", cv2.WINDOW_NORMAL)

qr_codes = set() 

while True:
    ret, frame = cap.read()

    decoded_objects = decode(frame)

    for obj in decoded_objects:
        qr_data = obj.data.decode('utf-8')
        if qr_data not in qr_codes: 
            print(qr_data)

            pygame.mixer.music.load("sesDosyasi.mp3")
            pygame.mixer.music.play()

            qr_codes.add(qr_data)  

    cv2.imshow("Kamera Görüntüsü", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
