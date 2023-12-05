import cv2


def getContours(img):
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3:
                objectType = "Tri"
            elif objCor == 4:
                aspRatio = w / float(h)
                if aspRatio > 0.98 and aspRatio < 1.03:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor > 4:
                objectType = "Circles"
            else:
                objectType = "None"

            # cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                imgContour,
                objectType,
                (x + (w // 2) - 10, y + (h // 2) - 10),
                cv2.FONT_HERSHEY_COMPLEX,
                0.7,
                (0, 0, 0),
                2,
            )


"""img = cv2.imread("./shapes.png")
if img is None:
    pass
else:
    imgContour = img.copy()
"""

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    if img is None:
        break
    imgContour = img.copy()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)

    getContours(imgCanny)
    cv2.imshow("Contour", imgContour)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
