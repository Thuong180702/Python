import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QGraphicsScene,
)
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image
from Image_Thresholding import Ui_MainWindow
from PyQt5.uic import loadUi
import matplotlib.pyplot as plt
import cv2
import numpy as np
import io


class MainWindow:
    # Khởi tạo ban đầu
    def __init__(self):
        self.myapp = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.myapp)

        self.uic.pushButton.clicked.connect(self.Openimage)
        self.uic.Slider_1.valueChanged.connect(self.update_line)
        self.uic.Slider_2.valueChanged.connect(self.update_line)
        self.uic.lineEdit.editingFinished.connect(self.update_slider)
        self.uic.lineEdit_2.editingFinished.connect(self.update_slider)
        self.uic.label_10.setScaledContents(
            True
        )  # cho phép hình ảnh tự động co giãn để vừa với kích thước của label_10
        self.uic.label_11.setScaledContents(True)

    def show(self):
        self.myapp.show()

    def update_slider(self):
        # slider1
        self.minvalue = float(self.uic.lineEdit.text())
        if self.uic.Slider_1.minimum() <= self.minvalue <= self.uic.Slider_1.maximum():
            self.uic.Slider_1.setValue(self.minvalue)
        else:
            self.uic.lineEdit.setText(f"{self.uic.Slider_1.value()}")
        # slider2
        self.maxvalue = float(self.uic.lineEdit_2.text())
        if self.uic.Slider_2.minimum() <= self.maxvalue <= self.uic.Slider_2.maximum():
            self.uic.Slider_2.setValue(self.maxvalue)
        else:
            self.uic.lineEdit_2.setText(f"{self.uic.Slider_2.value()}")
        Change(self)

    def update_line(self):
        self.minvalue = self.uic.Slider_1.value()
        self.uic.lineEdit.setText(f"{self.minvalue}")

        self.maxvalue = self.uic.Slider_2.value()
        self.uic.lineEdit_2.setText(f"{self.maxvalue}")
        Change(self)

    def Openimage(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter(
            "Image Files (*.png *.jpg *.bmp)"
        )  # chỉ có các tệp có định dạng .png, .jpg, hoặc .bmp sẽ được hiển thị và chọn được.
        file_dialog.setViewMode(QFileDialog.Detail)

        if (
            file_dialog.exec_()
        ):  # chọn một tệp và nhấn "OK", hàm này trả về True, ngược lại sẽ trả về False.
            image_path = file_dialog.selectedFiles()[0]

            if image_path:
                self.image = QImage(image_path)

            self.uic.Slider_1.valueChanged.connect(self.update_line)
            self.uic.Slider_2.valueChanged.connect(self.update_line)
            self.uic.lineEdit.editingFinished.connect(self.update_slider)
            self.uic.lineEdit_2.editingFinished.connect(self.update_slider)

            self.uic.label_10.setPixmap(QPixmap.fromImage(self.image))
            self.gray_image = self.image.convertToFormat(
                QImage.Format.Format_Grayscale8
            )

            Change(self)


def Change(self):
    try:
        # Chuyển ảnh RGB thành NumPy array
        width = self.image.width()
        height = self.image.height()

        ptr = self.image.constBits()
        ptr.setsize(self.image.byteCount())
        RGB_array = np.array(ptr).reshape(height, width, 4)

        # Tách các kênh màu
        r_values = RGB_array[:, :, 0].ravel()
        g_values = RGB_array[:, :, 1].ravel()
        b_values = RGB_array[:, :, 2].ravel()

        # Vẽ đồ thị tần số
        plt.figure(figsize=(6, 2))

        plt.hist(
            r_values,
            bins=256,
            range=(0, 256),
            color="red",
            alpha=0.7,
            label="Red Channel",
            histtype="step",
        )
        plt.hist(
            g_values,
            bins=256,
            range=(0, 256),
            color="green",
            alpha=0.7,
            label="Green Channel",
            histtype="step",
        )
        plt.hist(
            b_values,
            bins=256,
            range=(0, 256),
            color="blue",
            alpha=0.7,
            label="Blue Channel",
            histtype="step",
        )

        plt.title("Histogram of Original image")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.legend()

        buf1 = io.BytesIO()
        plt.savefig(buf1, format="png" or "jpg")  # Lưu đồ thị dưới dạng PNG hoặc JPG
        buf1.seek(0)

        image1 = QImage.fromData(buf1.getvalue())  # Chuyển đổi từ buffer sang QImage
        pixmap1 = QPixmap.fromImage(image1)

        # Hiển thị đồ thị trong QGraphicsView
        scene1 = QGraphicsScene()
        scene1.addPixmap(pixmap1)
        self.uic.graphicsView_2.setScene(scene1)

        plt.close()  # Đóng cửa sổ đồ thị

    except Exception as e:
        print(str(e))

        # Đồ thị tần số của ảnh Binary
    try:
        # Chuyển ảnh grayscale thành NumPy array
        width = self.gray_image.width()
        height = self.gray_image.height()

        ptr = self.gray_image.constBits()
        ptr.setsize(self.gray_image.byteCount())
        # Chuyển ảnh grayscale thành NumPy array
        gray_arr = np.array(ptr).reshape(height, width)

        # Đặt ngưỡng cho ảnh grayscale
        _, binary_arr = cv2.threshold(
            gray_arr, self.minvalue, self.maxvalue, cv2.THRESH_BINARY
        )
        # Tạo QImage mới từ dữ liệu nhị phân
        binary_qimage = QImage(
            binary_arr, width, height, QImage.Format.Format_Grayscale8
        )
        # Hiển thị ảnh nhị phân trên label
        self.uic.label_11.setPixmap(QPixmap.fromImage(binary_qimage))

        # Tính toán histogram
        histogram = cv2.calcHist([binary_arr], [0], None, [256], [0, 256])

        plt.figure(figsize=(6, 2))

        # Vẽ đồ thị tần số
        plt.plot(histogram)  # Được sử dụng để vẽ biểu đồ đường từ dữ liệu histogram
        plt.title("Histogram of Thresholded Image")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.tight_layout()

        buf = io.BytesIO()
        plt.savefig(
            buf, format="png" or "jpg"
        )  # Lưu đồ thị dưới định dạng PNG hoặc JPG
        buf.seek(0)

        image = QImage.fromData(buf.getvalue())  # Chuyển đổi từ buffer sang QImage
        pixmap = QPixmap.fromImage(image)

        # Hiển thị đồ thị trong QGraphicsView

        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.uic.graphicsView.setScene(scene)

        plt.close()  # Đóng cửa sổ đồ thị
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
