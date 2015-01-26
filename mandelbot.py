#!/usr/bin/env python

from PIL import Image
import tweepy
import time
import random
import os
from settings import *
from local_settings import *
from colors import ColorGenerator


class MandelBot():
    """
    This script creates an image of the mandelbrot set with
    a random color scheme and posts it to Twitter.

    2014
    Tobin Brown
    """

    def __init__(self):
        #Get the random rgb values for coloring
        self.generator = ColorGenerator(64)
        self.rgb = self.generator.random_rgb()
        #self.rgb.sort(key = lambda row: row[0] + row[1] + row[2])
        self.message = self.generator.message

    def generate_image(self):
        """
        Creates an image of the mandelbrot set and saves it to a
        file. Runs the algorithm to generate the set, applies
        the colors to the image, and saves the image
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
                r = self.rgb[i%64][0]
                g = self.rgb[i%64][1]
                b = self.rgb[i%64][2]
                mtx[x, y] =  r,g,b

        #Save the image
        name = self.image_name()
        image.save(name, "PNG")
        return self.name

    def image_name(self):
        millis = int(round(time.time() * 1000))
        directory = os.path.dirname(os.path.realpath(__file__))
        self.name = "{0}/images/mandelb0t_{1}.png".format(directory, millis)
        return self.name

    def send_tweet(self):
        #Make the OAuth connection
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.secure = True
        auth.set_access_token(access_token, access_token_secret)

        #Connect to the API
        self.api = tweepy.API(auth)
        #Tweet the status with the image
        self.api.update_with_media(image, status=str(self.message))


bot = MandelBot()
image = bot.generate_image()
bot.send_tweet()
