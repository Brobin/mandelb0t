# mandelb0t
Twitter bot that generates an image of the Mandelbrot set and posts it to the Twitters!

I built this real quick one day for fun and to make use of some new libraries and play around with images. Much thanks to [Andrew Lewis ](http://code.activestate.com/recipes/577111-mandelbrot-fractal-using-pil/) for the beautiful optimized code for generating the mandelbrot set.

I slightly modified the generation of colors so they are pseudo-random each day. I'm considering seeding it more in the future (maybe based on the weather or something, idk).

To run it yourself, install the dependencies and then fill out the settings with your own api access keys.

Dependencies
- tweepy
- PIL
