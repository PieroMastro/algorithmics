from PIL import Image, ImageFilter, ImageEnhance

with Image.open('original.jpg') as pic_original:
    print(f'Size: {pic_original.size}')
    print(f'Format: {pic_original.format}')
    print(f'Type: {pic_original.mode}')
    pic_original.show()

    pic_gray = pic_original.convert('L')   
    pic_gray.save('grey.jpg')
    print(f'Size: {pic_gray.size}')
    print(f'Format: {pic_gray.format}')
    print(f'Type: {pic_gray.mode}')
    pic_gray.show()

    blurred = pic_original.filter(ImageFilter.BLUR)
    blurred.save('blur.jpg')
    blurred.show()
    
    up = pic_original.transpose(Image.ROTATE_90)
    up.save('up.jpg')
    up.show()

    mirror = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    mirror.save('mirror.jpg')
    mirror.show()
