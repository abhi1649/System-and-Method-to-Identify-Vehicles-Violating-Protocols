# Improting Image class from PIL module
from PIL import Image
  
# Opens a image in RGB mode
im = Image.open(r"plate.jpg")
  
# Size of the image in pixels (size of orginal image)
# (This is not mandatory)
width, height = im.size
  
# Setting the points for cropped image
left = 6
top = height / 14
right = 72
bottom = 3 * height / 6
  
# Cropped image of above dimension
# (It will not change orginal image)
im1 = im.crop((left, top, right, bottom))
im1.save('seg.png')
# Shows the image in image viewer
im1.show()