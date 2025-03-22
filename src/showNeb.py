import os
from PIL import Image, ImageEnhance
from image_sources import img_utils


from epaper import epd 

if not os.path.isfile("./IMGP8320.JPG"):
    print("Image not found")
    return

self.processed_image = Image.open("./IMGP8320.JPG")
print("got the image")

img_utils.resize_image(self.original_image, 800, 480)

print("resized the image")

# Since the colors of epaper displays are fairly bleak, 
# we're brightening them up just a little bit.
try:
    converter = ImageEnhance.Color(self.processed_image)
    self.processed_image = converter.enhance(1.3)
    print("colour-corrected the image")
except:
    print("Failed to color-correct the image!")


epd.display(self.processed_image)
