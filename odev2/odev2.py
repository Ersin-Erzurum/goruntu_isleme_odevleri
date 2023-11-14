import cv2
import numpy as np

# Video girişi için kamera tanımlaması
cap = cv2.VideoCapture(0)

while True:
    # Giriş karesini oku
    ret, frame = cap.read()

    # Giriş karesini HSV renk uzayına dönüştür

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığını belirleme (HSV formatında)
    lower_red = np.array([0, 200, 20])
    upper_red = np.array([10, 255, 255])

    # HSV formatındaki renk aralığını kullanarak bir maske oluştur
    maske = cv2.inRange(hsv, lower_red, upper_red)

    # Orijinal görüntü üzerinde sadece kırmızı nesneleri gösteren bir maske oluştur
    sonuc = cv2.bitwise_and(frame, frame, mask=maske)

    # Görüntüyü göster
    cv2.imshow('ORJINAL', frame)
    cv2.imshow('SONUC', sonuc)

    # Çıkış için 'ESC' tuşuna basma kontrolü
    if cv2.waitKey(1) & 0xFF == 27: 
        break

# Kamera kullanımını kapat
cap.release()

# Pencereleri kapat
cv2.destroyAllWindows()