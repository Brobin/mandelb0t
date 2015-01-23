import random

class ColorGenerator():
    """
    This class is used to generate and array of rgb color combinations
    It contains methods that allow it to do so completely randomly,
    based on a random color, or on a provided color.
    """

    def __init__(self, elements=64, seed=None):
        self.elements = elements
        if seed is None:
            seed = self.generate_seed()
        self.seed = seed

    def generate_seed(self):
        """
        Generates an seed color to be used to generate the 
        set of colors. It does this by randomly choosing 
        each part of the RGB set.
        """
        self.seed = []
        self.seed.append(random.randint(0,256))
        self.seed.append(random.randint(0,256))
        self.seed.append(random.randint(0,256))
        return self.seed

    def random_rgb(self):
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

    def random_seeded_rgb(self):
        """
        Generates a set of colors based on a passed in color.
        Half random, half seed. Alternates light and dark
        shades to make layers more distinguishable.
        """
        rgb = []
        dark = True
        for x in range(0,self.elements):
            min = (0 if dark else 128)
            max = (128 if dark else 256)
            dark = (False if dark else True)
            r = (random.randint(min, max) + self.seed[0]) / 2
            g = (random.randint(min, max) + self.seed[1]) / 2
            b = (random.randint(min, max) + self.seed[2]) / 2
            rgb.append([r,g,b])
        return rgb
