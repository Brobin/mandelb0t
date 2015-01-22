
from PIL import Image
import tweepy
import time
import random
from settings import *
from local_settings import *


#Make the OAuth connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

#Connect to the API
api = tweepy.API(auth)

def mandelbrot():
    """
    Creates an image of the mandelbrot set
    """
    xa = -2.0
    xb = 1.0
    ya = -1.5
    yb = 1.5
    max_iterations = 256
    size = 512

    #Create a new image
    image = Image.new("RGB", (size, size))
    mtx = image.load()

    lutx = [j * (xb-xa) / (size - 1) + xa for j in xrange(size)]

    #Get the random rgb values for coloring
    rgb = random_rgb()

    for y in xrange(size):
        cy = y * (yb - ya) / (size - 1)  + ya
        for x in xrange(size):
            c = complex(lutx[x], cy)
            z = 0
            for i in xrange(max_iterations):
                if abs(z) > 2.0: break 
                z = z * z + c
            #Color the layer i
            r = rgb[0][i]
            g = rgb[1][i]
            b = rgb[2][i]
            mtx[x, y] =  r,g,b

    #Save the image
    millis = int(round(time.time() * 1000))
    name = "images/mandelb0t_{0}.png".format(millis)
    image.save(name, "PNG")
    return name

def random_rgb():
    """
    Generates an array of random RGB combinations
    """
    rgb = [[],[],[]]
    for x in range(0,256):
        rgb[0].append(random.randint(1,256))
        rgb[1].append(random.randint(1,256))
        rgb[2].append(random.randint(1,256))
    return rgb

name = mandelbrot()

#Tweet the status with the image
api.update_with_media(name)