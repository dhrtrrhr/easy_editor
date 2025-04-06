from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import *
from PIL import Image, ImageEnhance, ImageFilter
import os
app = QApplication([])


window = QWidget()
window.resize(800, 600)

def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap

main_line = QHBoxLayout()


left_line = QVBoxLayout()


folders_btn = QPushButton("Папка")
left_line.addWidget(folders_btn)


file_list = QListWidget()
file_list.addItems(["bright.png", "field.png", "trees.png", "villiage.png"])
left_line.addWidget(file_list)


v1_line = QVBoxLayout()


img_lbl = QLabel()

v1_line.addWidget(img_lbl)

btn_layout = QHBoxLayout()
btn_layout2 = QHBoxLayout()
btn_layout3 = QHBoxLayout()

left_btn = QPushButton("Вліво")
right_btn = QPushButton("Вправо")
mirror_btn = QPushButton("Дзеркало")
sharp_btn = QPushButton("Різкість")
bw_btn = QPushButton("Ч/Б")
enhence_btn = QPushButton("насиченість +")
EDGE_ENHANCE_btn = QPushButton("покращення ребер")
CONTOUR_btn = QPushButton("накладання контурів")
BLUR_btn = QPushButton("розмивання")
Brightness_btn = QPushButton("яскравість +")
DETAIL_btn =QPushButton("детелізація +")
SMOOTH_btn = QPushButton("згладжування")


btn_layout.addWidget(left_btn)
btn_layout.addWidget(right_btn)
btn_layout.addWidget(mirror_btn)
btn_layout.addWidget(sharp_btn)
btn_layout.addWidget(bw_btn)
btn_layout2.addWidget(enhence_btn)
btn_layout2.addWidget(EDGE_ENHANCE_btn)
btn_layout2.addWidget(CONTOUR_btn)
btn_layout2.addWidget(BLUR_btn)
btn_layout3.addWidget(Brightness_btn)
btn_layout2.addWidget(SMOOTH_btn)
btn_layout3.addWidget(DETAIL_btn)


v1_line.addLayout(btn_layout)
v1_line.addLayout(btn_layout2)
v1_line.addLayout(btn_layout3)



main_line.addLayout(left_line)
main_line.addLayout(v1_line)

class ImageProcessor:
    def __init__(self):
        self.folder = ""
        self.filename = ""
        self.image = ""

    def load(self):
        image_pass = os.path.join(self.folder, self.filename)
        self.image = Image.open(image_pass)

    def show(self):
        pix = pil2pixmap(self.image)
        pix = pix.scaledToWidth(500)
        img_lbl.setPixmap(pix)

    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.show()
    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.show()
    def flip_Left_Right(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.show()
    def sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.show()
    def Black_WHITE(self):
        self.image = self.image.convert("L")
        self.show()
    def enhence(self):
        self.image = ImageEnhance.Color(self.image).enhance(1.5)
        self.show()
    def edge_enhance(self):
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE)
        self.show()
    def CONTOUR(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)
        self.show()
    def BLUR(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.show()
    def Brightness(self):
        self.image =  ImageEnhance.Brightness(self.image).enhance(1.5)
        self.show()
    def DETAIL(self):
        self.image = self.image.filter(ImageFilter.DETAIL  )
        self.show()
    def SMOOTH(self):
        self.image = self.image.filter(ImageFilter.SMOOTH   )
        self.show()




ip = ImageProcessor()
ip.filename = "img.png"
ip.load()
ip.show()

def open_folders():
    ip.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(ip.folder)
    file_list.clear()
    for file in files:
        if file.endswith(".jpg"):
            file_list.addItem(file)
folders_btn.clicked.connect(open_folders)

def show_img():
    ip.filename = file_list.currentItem().text()
    ip.load()
    ip.show()
file_list.currentRowChanged.connect(show_img)



left_btn.clicked.connect(ip.rotate_left)
right_btn.clicked.connect(ip.rotate_right)
mirror_btn.clicked.connect(ip.flip_Left_Right)
sharp_btn.clicked.connect(ip.sharpen)
bw_btn.clicked.connect(ip.Black_WHITE)
enhence_btn.clicked.connect(ip.enhence)
EDGE_ENHANCE_btn.clicked.connect(ip.edge_enhance)
CONTOUR_btn.clicked.connect(ip.CONTOUR)
BLUR_btn.clicked.connect(ip.BLUR)
Brightness_btn.clicked.connect(ip.Brightness)
DETAIL_btn.clicked.connect(ip.DETAIL)
SMOOTH_btn.clicked.connect(ip.SMOOTH)


window.setLayout(main_line)


window.show()
app.exec()