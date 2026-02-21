#Metal colors
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
BRONZE = (205, 127, 50)


#Basic colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

#Pastel colors
PASTEL_PINK = (255, 182, 193)
PASTEL_BLUE = (173, 216, 230)
PASTEL_GREEN = (152, 251, 152)
PASTEL_YELLOW = (255, 255, 224)
PASTEL_PURPLE = (216, 191, 216)

#Neon colors
NEON_PINK = (255, 20, 147)
NEON_GREEN = (57, 255, 20)
NEON_BLUE = (0, 191, 255)
NEON_YELLOW = (255, 255, 0)
NEON_ORANGE = (255, 165, 0)
NEON_PURPLE = (148, 0, 211)

#Earth tones
BROWN = (139, 69, 19)
OLIVE = (128, 128, 0)
TAN = (210, 180, 140)
BEIGE = (245, 245, 220)
FOREST_GREEN = (34, 139, 34)
DARK_BLUE = (0, 0, 139)
MAROON = (128, 0, 0)
TEAL = (0, 128, 128)
NAVY = (0, 0, 128)
CHARCOAL = (54, 69, 79)

def darken_color(color, factor):
    r = max(0, int(color[0] * factor))
    g = max(0, int(color[1] * factor))
    b = max(0, int(color[2] * factor))
    return (r, g, b)

def lighten_color(color, factor):
    r = min(255, int(color[0] + (255 - color[0]) * factor))
    g = min(255, int(color[1] + (255 - color[1]) * factor))
    b = min(255, int(color[2] + (255 - color[2]) * factor))
    return (r, g, b)