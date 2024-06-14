from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = '/editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    #here the image at a certain path / the filename is opened so as to be edited
    box = (100, 100, 400, 400)
    edit = img.filter(ImageFilter.SHARPEN).rotate(90).convert('RGB')
    #the .crop() method crops the picture
    #keeping .convert('L') means the edited picture will be edited to black and white
    #keeping .convert('RGB') is for coloured images
    #the SHARPEN makes sure the picture is sharpened
    #if you want to rotate the picture you use .rotate(degrees you want the picture to rotate)
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    #if you want to increase the contrast of the picture to a certain value 
    clean_name = os.path.splitext(filename)[0]
    edit.save(f".{pathOut}/{clean_name}_edited.jpg")