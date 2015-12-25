from camera import *
import numpy as np
from PIL import Image
from geometry import *

# Global variables

HEIGHT = 550
WIDTH = 800

sence = []
sence.append(Sphere())

# set camera at P(0,0,0)
camera = Camera(HEIGHT, WIDTH)

# prepare the sences with group of primitives


##################################################
def scence_hit():



def ray_color():
    pass


##################################################
# main fun
image_array = np.zeros((HEIGHT, WIDTH))




# i for height j for width
for i in range(HEIGHT):
    for j in range(WIDTH):
        # do something for each pixel
        ray = camera.ray_generator(i, j)



im = Image.fromarray((np.uint8(image_array)))
im.show()

