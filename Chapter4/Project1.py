import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

myColors = {
    "Red": [0, 91, 157, 183, 244, 255],
    "Yello": [21, 71, 100, 70, 255, 172],
    "Green": [42, 89, 74, 106, 238, 179],
}


def findColor(result, color):
    imgHSV = cv2.cvtColor(result, cv2.COLOR_BGR2HSV)
    lower = np.array(color[0:3])
    upper = np.array(color[3:6])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(result, result, mask=mask)
    return imgResult


def get_key_from_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None


def getContours(imgResult, myColors, img):
    for color in myColors.values():
        imgResult = findColor(img, color)
        imgResult = cv2.cvtColor(imgResult, cv2.COLOR_BGR2GRAY)
        contours, hierarchy = cv2.findContours(
            imgResult, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
        )
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 100:
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
                x, y, w, h = cv2.boundingRect(approx)
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(
                    img,
                    get_key_from_value(myColors, color),
                    (x + (w // 2), y + (h // 2) - 10),
                    cv2.FONT_HERSHEY_COMPLEX,
                    0.7,
                    (255, 255, 255),
                    2,
                )


while True:
    success, img = cap.read()
    if img is None:
        break
    imgResult = img.copy()
    getContours(imgResult, myColors, img)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
