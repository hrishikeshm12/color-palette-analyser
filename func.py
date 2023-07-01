from colorthief import ColorThief
def get_palette(img):
    color_thief = ColorThief(img)
    palette = color_thief.get_palette(quality=1,color_count=11)
    return palette

def rgb_to_html_color(rgb):
    red, green, blue = rgb
    html_color = "#{:02x}{:02x}{:02x}".format(int(red), int(green), int(blue))
    return html_color