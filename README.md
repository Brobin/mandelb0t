# mandelb0t

Mandelb0t is a Twitter bot that generates an image of the Mandelbrot set and posts it to Twitter! Currently it functions as a cron job, running every two hours. Eventually I plan to host it somewhere where it can continuously run and interact with other Twitter users.

####Follow [@mandelb0t](https://twitter.com/mandelb0t) on Twitter!

### Mandelbrot Set

The [Mandelbrot Set](http://en.wikipedia.org/wiki/Mandelbrot_set) is a mathematical representation of complex numbers that when rendered can create beautiful images.

Thanks to [Andrew Lewis ](http://code.activestate.com/recipes/577111-mandelbrot-fractal-using-pil/) for the optimized code for generating the mandelbrot set.

### Coloring of the set

I slightly modified the generation of colors so they are random. First I randomly choose a base color in RBG (three numbers between 0 and 255). Then, I average each componenet of each color with another random number to generate 64 unique colors.

There are 256 layers in this rendering of the mandelbrot set, so each color is repeated once every 64 layers. Additionally, I added another factor to alternate between dark and light colors, making each layer more distinguishable.

This algorithm makes it so that there are 64*256^3 (1,073,741,824) possible color combinations for the mandelbrot set, essentially making each one completely unique.

### Examples!

Here are a couple of my favorites so far.

Purple

![](https://pbs.twimg.com/media/CByynw8UIAEU4-s.png)

Blue

![](https://pbs.twimg.com/media/CALzBRKUQAEpx-j.png)


