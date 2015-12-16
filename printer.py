from PIL import Image, ImageDraw
import colorsys

def image_rgb(image):
    r = g = b = 0
    numpix = image.size[0]*image.size[1]
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = image.getpixel((x,y))
            r += pixel[0]
            g += pixel[1]
            b += pixel[2]
    return (int(r/numpix),int(g/numpix),int(b/numpix))

def rgb_to_hsv(color):
    dec_hsv = colorsys.rgb_to_hsv(color[0]/255.0, color[1]/255.0, color[2]/255.0)
    #return (int(dec_hsv[0]*260), int(dec_hsv[1]*255), int(dec_hsv[2]*255))
    return (int(dec_hsv[0]*255), int(dec_hsv[1]*255), int(dec_hsv[2]*255))



class ImageSegment(object):
    def __init__(self, image, position):
        self.image = image
        self.hsv = rgb_to_hsv(image_rgb(self.image))
        self.position = (position[0]*self.image.size[0], position[1]*self.image.size[1])

input = Image.open("assets/test.jpg")
x_segments = 20
y_segments = 20
twidth = input.size[0]
theight = input.size[1]
swidth = twidth/x_segments
sheight = theight/y_segments

segments = []
for x in range(x_segments):
    for y in range (y_segments):
        box = (x*swidth, y*sheight, x*swidth+swidth, y*sheight+sheight)
        new_image = input.crop(box=box)
        new_image.load()
        position = (x,y)
        new_segment = ImageSegment(input.crop(box), position)
        segments.append(new_segment)

palette = Image.new("HSV", (twidth, theight))

for segment in segments:
    draw = ImageDraw.Draw(palette)
    rect = [segment.position, (segment.position[0]+swidth, segment.position[1]+sheight)]
    print segment.hsv
    #new_hsv = segment.hsv
    new_hsv = (segment.hsv[0], 200, 200)
    draw.rectangle(rect, fill=new_hsv, outline=new_hsv)

palette.convert("RGB").save("assets/final2.jpg")








