import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plt

img = cv2.imread("./car.jpg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rander = easyocr.Reader(["en"], gpu=False)
text = rander.readtext(img)
box, text, score = text[0]

cv2.rectangle(img, box[0], box[2], (255, 0, 0), 5)
cv2.putText(
    img,
    text,
    box[0],
    cv2.FONT_HERSHEY_COMPLEX,
    4.5,
    (0, 255, 0),
    5,
)

plt.imshow(img)
plt.show()
