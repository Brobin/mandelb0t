import random

class ColorGenerator():
    """
    This class is used to generate and array of rgb color combinations
    It contains methods that allow it to do so completely randomly,
    based on a random color, or on a provided color.
    """

    def __init__(self, elements=64, mix=None):
        self.elements = elements
        if mix is None:
            mix = self.generate_mix()
        self.mix = mix
        self.message = mix

    def random_rgb(self):
        method = random.randint(0,1)
        if method == 0:
            rgb = self.completely_random_rgb()
            self.message = "Completely random color scheme"
        else:
            rgb = self.random_mixed_rgb()
            self.message = "Random color scheme, based off of " + str(self.mix)
        sort = random.randint(0,1)
        if sort == 0:
            rgb = self.sort_light(rgb)
            self.message += ", sorted by lightness."
        else:
            rgb = self.sort_dark(rgb)
            self.message += ", sorted by darkness."
        return rgb

    def generate_mix(self):
        """
        Generates an mix color to be used to generate the 
        set of colors. It does this by randomly choosing 
        each part of the RGB set.
        """
        self.mix = []
        self.mix.append(random.randint(0,256))
        self.mix.append(random.randint(0,256))
        self.mix.append(random.randint(0,256))
        return self.mix

    def completely_random_rgb(self):
        """
        Generates a completely random set of colors. The nature of
        the randomness generally makes it so that the colors
        are very bright, obnoxious and non-matching.
        """
        rgb = []
        for x in range(0,self.elements):
            r = random.randint(0,256)
            g = random.randint(0,256)
            b = random.randint(0,256)
            rgb.append([r,g,b])
        return rgb

    def random_mixed_rgb(self):
        """
        Generates a set of colors based on a passed in color.
        Half random, half mix. Alternates light and dark
        shades to make layers more distinguishable.
        """
        rgb = []
        dark = True
        for x in range(0,self.elements):
            min = (0 if dark else 128)
            max = (128 if dark else 256)
            dark = (False if dark else True)
            r = (random.randint(min, max) + self.mix[0]) / 2
            g = (random.randint(min, max) + self.mix[1]) / 2
            b = (random.randint(min, max) + self.mix[2]) / 2
            rgb.append([r,g,b])
        return rgb

    def sort_light(self, rgb):
        """
        Creates a set of RBG colors roughly sorted by lightness.
        """
        rgb.sort(key=lambda x: 0.2126*x[0] + 0.7152*x[1] + 0.0722*x[2])
        return rgb

    def sort_dark(self, rgb):
        """
        Creates a set of RBG colors roughly sorted by darkness.
        """
        rgb.sort(key=lambda x: 255 - (0.2126*x[0] + 0.7152*x[1] + 0.0722*x[2]))
        return rgb
