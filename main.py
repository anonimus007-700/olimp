from PIL import Image
from random import randint

from config import *

################################################
###################CODING#######################
################################################

text = input()

image = Image.new('RGB',(15, 4000))

img0 = Coder.coding_script(text, image)

img0.save('cod.png', 'PNG')

################################################
##################DECODING######################
################################################

image = Image.open('cod.png')

print(Decoder.decoding_script(image))

################################################
#################PLACER_CODING##################
################################################

img1 = Image.open("zxc.jpg")
img2 = Image.open("cod.png")

pos1 = randint(0, img1.size[0])
pos2 = randint(0, img1.size[1])

if pos1 > img2.size[0]:
    pos1 -= img2.size[0]

if pos2 > img2.size[1]:
    pos2 -= img2.size[1]

str_pos = str(pos1) + ' ' + str(pos2) + ' ' + str(pos1+img2.size[0]) + ' ' + str(pos2+img2.size[1])
img = Coder.coding_script(str_pos, Image.new("RGB", img1.size), True)

str_pos = str(pos1) + ' ' + str(pos2+img.height) + ' ' + str(pos1+img2.size[0]) + ' ' + str(pos2+img2.size[1]+img.height)
img = Coder.coding_script(str_pos, Image.new("RGB", img1.size), True)

img1.paste(img2, (pos1, pos2))

framed_image = Image.new("RGB", (img1.size[0], img1.height + 1))

framed_image.paste(img1, (0, 1))
framed_image.paste(img)

framed_image.save('output.png')

################################################
################PLACER_DECODING#################
################################################

img = Image.open("output.png")

x1, y1, x2, y2 = map(int, Decoder.decoding_script(img).split())

img = img.crop((x1, y1, x2, y2))

print(Decoder.decoding_script(img))
