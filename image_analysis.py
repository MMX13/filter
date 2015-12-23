import colourx
from PIL import Image


def image_hcl(Image):
    r = g = b = 0.0
    numpix = Image.width * Image.height

    for y in range(Image.height):
        for x in range(Image.width):
            pixel = Image.getpixel((x,y))
            r += pixel[0]
            g += pixel[1]
            b += pixel[2]
    avg_rgb = (r/numpix, g/numpix, b/numpix)
    return colourx.rgb_to_hcl(avg_rgb)


