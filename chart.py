from PIL import Image
import colorsys
import colourx

depth = 256

colours = {}

def print_hsv_hv_colour():
    chart = Image.new("HSV", (depth, depth))

    for v in range(depth):
        for h in range(depth):
            chart.putpixel((h,depth-1-v), (h,255,v))

    chart.convert("RGB").save("assets/hsvhvcolour.jpg")

def print_hsv_hv_grey():
    chart = Image.new("HSV", (depth, depth))

    for v in range(depth):
        for h in range(depth):
            rgb = colorsys.hsv_to_rgb(h/255.0,1,v/255.0)
            chart.putpixel((h,depth-1-v), (0, 0, colourx.get_lum((rgb[0]*255, rgb[1]*255, rgb[2]*255))))

    chart.convert("RGB").save("assets/hsvhvgrey.jpg")

def print_hcl_hl_colour():
    chart = Image.new("RGB", (depth, depth))

    for l in range(depth):
        for h in range(depth):
            rgb = colourx.hcl_to_rgb((h, 255, l))
            chart.putpixel((h, depth-1-l), rgb)
    chart.convert("RGB").save("assets/hclhlcolour.bmp")

def print_hcl_hl_grey():
    chart = Image.new("HSV", (depth, depth))

    for l in range(depth):
        for h in range(depth):
            rgb = colourx.hcl_to_rgb((h, 255, l))
            chart.putpixel((h, depth-1-l), (0,0,colourx.get_lum(rgb)))

    chart.convert("RGB").save("assets/hclhlgrey.bmp")

def hsv_rainbow():
    chart = Image.new("HSV", (depth, 100))

    for i in range(100):
        for h in range(depth):
            rgb = (h, 255, 255)
            chart.putpixel((h, 99-i), rgb)

    chart.convert("RGB").save("assets/rainbowhsv.bmp")


def hcl_rainbow():
    chart = Image.new("RGB", (depth, 100))

    for i in range(100):
        for h in range(depth):
            rgb = colourx.hcl_to_rgb((h, 255, 255))
            chart.putpixel((h, 99-i), rgb)

    chart.convert("RGB").save("assets/rainbowhcl.bmp")

if __name__ == "__main__":
    print_hsv_hv_colour()
    print_hsv_hv_grey()
    print_hcl_hl_colour()
    print_hcl_hl_grey()
    hsv_rainbow()
    hcl_rainbow()