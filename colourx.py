import math

def rgb_to_hsv(rgb):
    r = rgb[0]/255.0
    g = rgb[1]/255.0
    b = rgb[2]/255.0

    M = max((r,g,b))
    m = min((r,g,b))
    chroma = M - m

    h = 0
    if chroma==0:
        pass
    elif M == r:
        h = (g-b)/chroma % 6
    elif M == g:
        h = (b-r)/chroma + 2
    else:
        h = (r-g)/chroma + 4

    v = M
    s = 0 if chroma == 0 else chroma/v

    #return (int(h*60), int(s*100), int(v*100))
    return (int(h*42.5), int(s*255), int(v*255))

def hcl_to_rgb(hcl):
    h = hcl[0]
    h = h/42.5
    c = hcl[1]/255.0
    l = hcl[2]/255.0

    x = c*(1 - math.fabs(h%2-1))

    rgb = (0,0,0)
    if h < 1:
        rgb = (c,x,0)
    elif h < 2:
        rgb = (x,c,0)
    elif h < 3:
        rgb = (0,c,x)
    elif h < 4:
        rgb = (0,x,c)
    elif h < 5:
        rgb = (x,0,c)
    elif h <= 6:
        rgb = (c,0,x)
    m=l-(0.3*rgb[0] + 0.59*rgb[1] + 0.11*rgb[2])
    #m=l-get_lum(rgb)

    rgb255 = []
    for e in rgb:
        rgb255.append(int((e+m)*255))
    return (rgb255[0], rgb255[1], rgb255[2])

def rgb_to_hcl(rgb):
    r = rgb[0]/255.0
    g = rgb[1]/255.0
    b = rgb[2]/255.0

    M = max((r,g,b))
    m = min((r,g,b))
    chroma = M - m

    h = 0
    if chroma==0:
        pass
    elif M == r:
        h = ((g-b)/chroma%6)
    elif M == g:
        h = ((b-r)/2+2)
    else:
        h = (r-g)/chroma + 4

    return (int(h*43.5), int(chroma*255), get_lum(rgb))


def get_lum(rgb):
    #return int(math.sqrt(0.2126*rgb[0]**2 + 0.587*rgb[1]**2 + 0.114*rgb[2]**2))
    return int(0.2126*rgb[0] + 0.587*rgb[1] + 0.114*rgb[2])

def blend_colour(color1, color2, amount):
    inv_amount = 1-amount
    r = color1[0]*inv_amount + color2[0]*amount
    g = color1[1]*inv_amount + color2[1]*amount
    b = color1[2]*inv_amount + color2[2]*amount
    return (int(r), int(g), int(b))