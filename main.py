from myClass import *
import numpy as np
from PIL import Image

# Global variables

HEIGHT = 550
WIDTH = 800


# set camera at P(0,0,0)
camera = Camera(HEIGHT, WIDTH)

# prepare the sences with group of primitives



# main
image_array = np.zeros((HEIGHT, WIDTH))

# i for height j for width
for i in range(HEIGHT):
    for j in range(WIDTH):
        # do something for each pixel
        ray = camera.ray_generator(i, j)



im = Image.fromarray((np.uint8(image_array)))
im.show()

