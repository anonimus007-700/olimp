from PIL import Image

from config import *

################################################
###################CODING#######################
################################################

text = input()

image = Image.new('RGB',(1500, 4000))

pixels = image.load()

text = Coder.text_to_cod(text)

x, y = 0, 0

for cod in text:
    for i in cod:
        if x+1 < image.size[0]:
            if i == '1':
                pixels[x, y] = (255,255,255)
            else:
                pixels[x, y] = (0,0,0)
            x = x + 1
        elif x+1 >= image.size[0]:
            if i == '1':
                pixels[x, y] = (255,255,255)
            else:
                pixels[x, y] = (0,0,0)
            y = y + 1
            x = 0

    if x+1 < image.size[0]:
        pixels[x, y] = (1,0,0)
        x = x + 1
    elif x+1 >= image.size[0]:
        pixels[x, y] = (1,0,0)
        y = y + 1
        x = 0

image = image.crop((0, 0, 1500, y+1))

image.save('cod.png', 'PNG')

################################################
##################DECODING######################
################################################

cod = []

image = Image.open('cod.png')

for y in range(image.size[1]):
    for x in range(image.size[0]):
        if image.getpixel((x, y)) == (0,0,0):
            cod.append(0)
        elif image.getpixel((x, y)) == (1,0,0):
            cod.append(3)
        else:
            cod.append(1)

cod = [str(num) for num in cod]

cod = ''.join(cod)

cod = cod.split('3')

print(''.join(Decoder.int_to_text(cod)))


