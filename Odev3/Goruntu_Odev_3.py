import cv2
import numpy as np
import os

file_path = os.path.realpath(__file__)
folder, file_name = os.path.split(file_path)
image_path = folder + '\\' + 'pirinclerFoto.jpg'  

# Resmi oku
img = cv2.imread(image_path)

# Resmi griye çevir
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Pirinç Tnaelerini eşikle
_, thresholded_image = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY)

# Gereksiz arka planı sil
kernel = np.ones((5, 5), np.uint8)
morphological_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_CLOSE, kernel)

# Pirinçleri say
contours, _ = cv2.findContours(morphological_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rice_count = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100:
        rice_count += 1

# Açılacak olan pencere boyutları
window_width = 600
window_height = 600

cv2.namedWindow('Pencere2', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Pencere2', window_width, window_height)

cv2.imshow('Pencere2', morphological_image)

print(f"Pirinç sayısı: {rice_count}")

cv2.waitKey(0)
cv2.destroyAllWindows()
