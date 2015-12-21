from PIL import Image
import colorsys
import colourx

depth = 256

colours = {}

def hslum_gen():
    for r in range(255):
        for g in range(255):
            for b in range(255):
                print(str((r,g,b)))
                hsv = colourx.rgb_to_hsv((r,g,b))
                lum = colourx.get_lum((r,g,b))
                colours[(hsv[0],hsv[1], lum)] = hsv

class Colour():
    def __init__(self, rgb):
        self.rgb = rgb
        #self.hsv = hsv
        #self.lum = colourx.get_lum(rgb)
        #self.hslum = (self.hsv[0], self.hsv[1], colourx.get_lum(rgb))

def generate_color_map():
    for r in range(255):
        for g in range(255):
            for b in range(255):
                rgb = (r, g, b)
                print("Generating "+str(rgb))
                #hsv = colourx.rgb_to_hsv(rgb)
                new_colour = Colour(rgb)
                colours.append(new_colour)

def print_colour_map():
    chart = Image.new("RGB", (depth, depth))

    x = y = 0
    for colour in colours:
        chart.putpixel((x,y), colour.rgb)
        x+=1
        if x==depth:
            x = 0
            y+=1
    chart.save("assets/colormap.bmp")

def print_color_chart():
    chart = Image.new("HSV", (depth, depth))

    for s in range(depth):
        for h in range(depth):
            chart.putpixel((h,depth-1-s), (h,s,255))

    chart.convert("RGB").save("assets/colorchart2.jpg")

def print_grey_chart():
    chart = Image.new("HSV", (depth, depth))

    for s in range(depth):
        for h in range(depth):
            rgb = colorsys.hsv_to_rgb(h/255.0,s/255.0,1)
            color = SCP((int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)))
            chart.putpixel((h,depth-1-s), (0, 0, color.brightness))

    chart.convert("RGB").save("assets/greychart.jpg")

def uniform_grey_chart():
    chart = Image.new("HSV", (depth, depth))

    for s in range(depth):
        for h in range(depth):
            rgb = colorsys.hsv_to_rgb(h/255.0,s/255.0,1)
            color = SCP((int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)))
            if color.brightness>245:
                chart.putpixel((h,depth-1-s), (0, 0, color.brightness))
            else:
                chart.putpixel((h,depth-1-s), (0, 0, 0))

    chart.convert("RGB").save("assets/ugreychart.jpg")

def print_hl_chart():
    chart = Image.new("HSV", (depth, depth))

    for l in range(depth):
        for h in range(depth):
            chart.putpixel((h, depth-1-l), (h, 255, l))

    chart.convert("RGB").save("assets/hlchart.jpg")

def print_hl_grey_chart():
    chart = Image.new("HSV", (depth, depth))

    for l in range(depth):
        for h in range(depth):
            rgb = colorsys.hsv_to_rgb(h/255.0,1,l/255.0)
            color = SCP((int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255)))

            chart.putpixel((h,depth-1-l), (0, 0, color.brightness))

    chart.convert("RGB").save("assets/hlgreychart.jpg")


def print_hcl_chart():
    chart = Image.new("RGB", (depth, depth))

    for c in range(depth):
        for h in range(depth):
            rgb = colourx.hcl_to_rgb((h, c, 100))
            chart.putpixel((h, depth-1-c), rgb)
    chart.save("assets/hcl.bmp")

def print_hcl_c_chart():
    chart = Image.new("RGB", (depth, depth))

    for l in range(depth):
        for h in range(depth):
            rgb = colourx.hcl_to_rgb((h, 100, l))
            chart.putpixel((h, depth-1-l), rgb)
    chart.save("assets/hclc.bmp")

def print_hcl_cl_chart():
    chart = Image.new("RGB", (depth, depth))

    for c in range(depth):
        for l in range(depth):
            rgb = colourx.hcl_to_rgb((100, c, l))
            chart.putpixel((c, depth-1-l), rgb)
    chart.save("assets/hclcl.bmp")

def print_hcl_hc_chart():
    chart = Image.new("RGB", (depth, depth))

    for c in range(depth):
        for h in range(depth):
            rgb = colourx.hcl_to_rgb((h, c, 200))
            chart.putpixel((h, depth-1-c), rgb)
    chart.save("assets/hclhl.bmp")

def print_conversions():
    chart = Image.new("HSV", (depth, depth))

    for r in range(depth):
        for g in range(depth):
            hsv = colourx.rgb_to_hsv((r, g, 100))
            chart.putpixel((r, depth-1-g), hsv)
    chart.convert("RGB").save("assets/convert.bmp")

def ugly_rainbow():
    chart = Image.new("HSV", (depth, 100))

    for i in range(100):
        for h in range(depth):
            hsv = (h, 255, 200)
            chart.putpixel((h, 99-i), hsv)

    chart.convert("RGB").save("assets/rainbowugly.bmp")


def nice_rainbow():
    chart = Image.new("RGB", (depth, 100))

    for i in range(100):
        for h in range(depth):
            hsv = colourx.hcl_to_rgb((h, 255, 100))
            chart.putpixel((h, 99-i), hsv)

    chart.convert("RGB").save("assets/rainbow.bmp")


class SCP():
    def __init__(self, color):
        self.rgb = color
        self.brightness = self.get_perceived_brightness(self.rgb)

    def get_perceived_brightness(self, color):
        return int((299*color[0]+587*color[1]+114*color[2])/1000)


if __name__ == "__main__":
    #print_color_chart()
    #print_grey_chart()
    #uniform_grey_chart()
    #print_hcl_cl_chart()
    #print_hl_grey_chart()
    #generate_color_map()
    #print_colour_map()
    #print_conversions()
    #print_hcl_hc_chart()
    nice_rainbow()
    ugly_rainbow()