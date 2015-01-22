import random

def random_pastel_rgb():
    """
    Generates an array of random RGB colors based on a random
    seed color. First it generates a rnadom color, then
    calls random_seed_rgb to get a set based on that.
    """
    rgb = []
    mix = []
    mix.append(random.randint(0,256))
    mix.append(random.randint(0,256))
    mix.append(random.randint(0,256))
    return random_seeded_rgb(mix)

def random_bright_rgb():
    """
    Generates a completely random set of colors. The nature of
    the randomness generally makes it so that the colors
    are very bright, obnoxious and non-matching.
    """
    rgb = []
    for x in range(0,64):
        r = random.randint(0,256)
        g = random.randint(0,256)
        b = random.randint(0,256)
        rgb.append([r,g,b])
    return rgb

def random_seeded_rgb(seed):
    """
    Generates a set of colors based on a passed in color.
    Half random, half seed. Alternates light and dark
    shades to make layers more distinguishable.
    """
    rgb = []
    dark = True
    for x in range(0,64):
        if dark:
            r = (random.randint(0,128) + seed[0]) / 2
            g = (random.randint(0,128) + seed[1]) / 2
            b = (random.randint(0,128) + seed[2]) / 2
            rgb.append([r,g,b])
            dark = False
        else:
            r = (random.randint(128,256) + seed[0]) / 2
            g = (random.randint(128,256) + seed[1]) / 2
            b = (random.randint(128,256) + seed[2]) / 2
            rgb.append([r,g,b])
            dark = True
    return rgb