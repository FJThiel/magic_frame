import os
from PIL import Image, ImageEnhance
from image_sources import img_utils


from epaper import waveshare_7_3_epd 

if os.path.isfile("./IMGP8320.JPG"):
    
    image = Image.open("./IMGP8320.JPG")
    print("got the image")

    processed_image = img_utils.resize_image(image, 800, 480)

    print("resized the image")

    # Since the colors of epaper displays are fairly bleak, 
    # we're brightening them up just a little bit.
    try:
        converter = ImageEnhance.Color(processed_image)
        processed_image = converter.enhance(1.3)
        print("colour-corrected the image")
    except:
        print("Failed to color-correct the image!")


    waveshare_7_3_epd.display(processed_image)


else:
    print("Image not found")
    