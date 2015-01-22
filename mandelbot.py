#!/usr/bin/env python

from PIL import Image
import tweepy
import time
import random
import os
from settings import *
from local_settings import *
from colors import *

"""
This script creates an image of the mandelbrot set with
a random color scheme and posts it to Twitter.

2014
Tobin Brown
"""


#Make the OAuth connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

#Connect to the API
api = tweepy.API(auth)

def mandelbrot():
    """
    Creates an image of the mandelbrot set and saves it to
    a file.
        1. Runs the algorithm to generate the image.
        2. Calls the rbg functions to get the color schemes.
        3. Applies colors to each layer
        4. Saves the image
        5. Returns the absolute file path of the image
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
    rgb = random_pastel_rgb()

    #Create the mandelbrot set
    for y in xrange(size):
        cy = y * (yb - ya) / (size - 1)  + ya
        for x in xrange(size):
            c = complex(lutx[x], cy)
            z = 0
            for i in xrange(max_iterations):
                if abs(z) > 2.0: break 
                z = z * z + c
            #Color the layer i
            r = rgb[i%64][0]
            g = rgb[i%64][1]
            b = rgb[i%64][2]
            mtx[x, y] =  r,g,b

    #Save the image
    millis = int(round(time.time() * 1000))
    directory = os.path.dirname(os.path.realpath(__file__))

    name = "{0}/images/mandelb0t_{1}.png".format(directory, millis)
    image.save(name, "PNG")

    return name

image = mandelbrot()

#Tweet the status with the image
api.update_with_media(image)