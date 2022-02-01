import PIL
from PIL import Image

Image.MAX_IMAGE_PIXELS = 1000000000 
#load image

# im = Image.open("01-01-01.png").convert('RGB')

# # Setting the points for cropped image
# left = 2000
# top = 100
# right = 10000
# bottom = 4000
 
# # Cropped image of above dimension
# # (It will not change original image)
# im1 = im.crop((left, top, right, bottom))
# # newsize = (300, 300)
# # im1 = im1.resize(newsize)
# # Shows the image in image viewer
# im1.save("cropped.png")







im = Image.open("cropped.png").convert('RGB')
width = int(input("width?"))
im = im.resize((width, int(width/2.05128205)))
im.save("lower_res_img.png")



