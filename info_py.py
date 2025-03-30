from PIL import Image


with Image.open("1920x.jpg")as pic_original:
    print("Зображення відкрито")
    print("Розмір:", pic_original.size)
    print("Формат:", pic_original.format)
    print("Режим:", pic_original.mode)
    pic_original.show()