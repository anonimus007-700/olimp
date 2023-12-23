from PIL import Image


class Coder:
    def text_to_cod(text):
        coding_text = []
        out_list = []
        for i in text:
            coding_text.append(str(ord(i)))
        for i in coding_text:
            out_list.append(bin(int(i))[2:])
        return out_list

    def coding_script(text, image, to_img=False):
        x, y = 0, 0
        
        text = Coder.text_to_cod(text)
        pixels = image.load()
        
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
        
        if to_img:
            pixels[x, y] = (255,0,255)

        image = image.crop((0, 0, image.size[0], y+1))
        
        return image
    
    def coding_to_place(text, image):
        image = Coder.coding_script(text, image)
        
        new_width = image.width + 2
        new_height = image.height + 2
        framed_image = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))
        
        framed_images = framed_image.load()
        
        framed_images[0, 0] = (0,1,0)
        framed_images[0, image.size[1]+1] = (0,1,0)
        framed_images[image.size[0]+1, 0] = (0,1,0)
        framed_images[image.size[0]+1, image.size[1]+1] = (0,1,0)

        framed_image.paste(image, (1, 1))

        return framed_image

class Decoder:
    def int_to_text(number):
        coding_text = []
        int_text = []
        for i in number:
            int_text.append(int(i, 2))
        for i in int_text:
            coding_text.append(chr(int(i)))
        
        coding_text = [item for item in coding_text if item != '\x00']
        return coding_text

    def decoding_script(image):
        cod = []
        found_pixel = False
        
        for y in range(image.height):
            for x in range(image.width):
                if image.getpixel((x, y)) == (0,0,0):
                    cod.append(0)
                elif image.getpixel((x, y)) == (1,0,0):
                    cod.append(3)
                elif image.getpixel((x, y)) == (255,0,255):
                    found_pixel = True
                    break
                else:
                    cod.append(1)

            if found_pixel:
                break

        cod = [str(num) for num in cod]
        cod = ''.join(cod)
        cod = cod.split('3')
        
        cod = list(filter(lambda item: item != '', cod))

        return ''.join(Decoder.int_to_text(cod))
    