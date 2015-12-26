from camera import *
import numpy as np
from PIL import Image
from geometry import *

# Global variables

# HEIGHT = 300
# WIDTH = 300

HEIGHT = 300
WIDTH = 300

# HEIGHT = 800
# WIDTH = 1000

std_t0 = 0.1
std_t1 = 1000000

# about light
Ia = 100
light_a = Light(Vector3(-1000, -100, 1000), 255)


# about scene
scene = []
scene.append(Ground())
scene.append(Sphere(Vector3(-150, 800, 150), 150))
scene.append(Sphere(Vector3(120, 800, 100), 100))


# set camera at P(0,0,0)
position = Vector3(-50, -100, 120)
up = Vector3(0, 0, 1)
view_re = Vector3(0, -1, 0)

#camera = Camera(HEIGHT, WIDTH, position, up, view_re)
camera = CameraV2(HEIGHT, WIDTH, position, 0)
# camera = Camera(HEIGHT, WIDTH)



##################################################
###############
def scene_hit(ray, t0, t1):
    global scene, light_a

    hit = False
    tt0 = t0
    tt1 = t1
    record = None

    for surface in scene:
        #print(surface.hit(ray, light_a, tt0, tt1))
        is_hit, t, rec = surface.hit(ray, light_a, tt0, tt1)


        if is_hit:
            hit = True
            record = rec
            tt1 = t
    return hit, tt1, record

################
def ray_color(ray, t0, t1, depth):
    # max recursive depth
    if depth > 5:
        return 0

    is_hit, t, rec = scene_hit(ray, t0, t1)

    if is_hit:
        # intersection point
        p = ray.origin.plus(ray.direction.s_multip(t))
        # color
        c = rec.Ka * Ia

        s_is_hit, s_t, s_rec = scene_hit(Ray(p, rec.l), t0, t1)

        # Ideal Specular Reflection
        K_isr = 0.2
        two_nv = 2 * rec.n.dot(rec.v)
        two_nvN = rec.n.s_multip(two_nv)
        r = two_nvN.minus(rec.v)

        c += K_isr * ray_color(Ray(p, r), t0, t1, depth+1)


        if not s_is_hit:
            h = rec.l.plus(rec.v)
            h.normalize()
            c += rec.Kd * rec.I * max(0, rec.n.dot(rec.l))
            c += rec.Ks * rec.I * (rec.n.dot(h)**rec.p)

        return c
    else:
        return 0


##################################################
# main fun
image_array = np.zeros((HEIGHT, WIDTH))


# i for height j for width
for i in range(HEIGHT):
    for j in range(WIDTH):
        # do something for each pixel
        i_ray = camera.ray_generator(i, j)
        color = ray_color(i_ray, std_t0, std_t1, 1)
        if color > 255:
            color = 255
        image_array[i, j] = color

im = Image.fromarray((np.uint8(image_array)))
im.show()
im.save("./pic/R.JPG", "JPEG")


