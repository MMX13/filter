from PIL import Image
import colorsys

depth = 256

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
    print_hl_chart()
    print_hl_grey_chart()