import colourx
import math
from PIL import Image

MINIMUM_SAT = 15  # Minimum amount of saturation when using saturation clamp

# Takes the input image and shifts the hue of every pixel to hue of the provided color.
def filter(image, rgb):
    filtered_image = Image.new("RGB", (image.width, image.height))
    for y in range(image.height):
        for x in range(image.width):
            pixel = colourx.rgb_to_hcl(image.getpixel((x,y)))
            new_hue = colourx.rgb_to_hcl(rgb)[0]
            new_color = (new_hue, pixel[1], pixel[2])
            filtered_image.putpixel((x,y), colourx.hcl_to_rgb(new_color))
    return filtered_image

# Takes the input image and shifts the hue of every pixel closer to the provided hue, based on saturation
def dynamic_filter(image, rgb, colour_clamp=False):
    filtered_image = Image.new("RGB", (image.width, image.height))
    for y in range(image.height):
        for x in range(image.width):
            opixel = image.getpixel((x,y))
            pixel = colourx.rgb_to_hcl(image.getpixel((x,y)))
            new_hue = colourx.rgb_to_hcl(rgb)[0]
            new_color = colourx.hcl_to_rgb((new_hue, pixel[1], pixel[2]))

            opacity = math.sqrt(255**2-opixel[1]**2)/255.0
            new_color = colourx.blend_colour( opixel, new_color, opacity)
            filtered_image.putpixel((x,y), new_color)

    return filtered_image

#Takes a value of range 0-255 and returns a value of range 15-255
def sat_clamp(sat):
    return int(round(sat/255.0*240+MINIMUM_SAT, 0))