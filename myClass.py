from functools import reduce
from math import sqrt

class Vector3:
    def __init__(self, x, y, z):
        self.px = x
        self.py = y
        self.pz = z

    def dot(self, v3):
        s = self.px * v3.px + self.py * v3.py + self.pz * v3.pz
        return s

    def X(self, v3):
        x = self.py * v3.pz - self.pz * v3.py
        y = self.pz * v3.px - self.px * v3.pz
        z = self.px * v3.py - self.py * v3.px
        return Vector3(x, y, z)

    def plus(self, v3):
        x = self.px + v3.px
        y = self.py + v3.py
        z = self.pz + v3.pz
        return Vector3(x, y, z)

    def minus(self, v3):
        x = self.px - v3.px
        y = self.py - v3.py
        z = self.pz - v3.pz
        return Vector3(x, y, z)

    def s_multip(self, k):
        x = k * self.px
        y = k * self.py
        z = k * self.pz
        return Vector3(x, y, z)


    def normalize(self):
        def f(x):
            return x**2
        def g(a,b):
            return a+b
        def h(a,b):
            return a/b

        mo = map(f, [self.px, self.py, self.pz])
        mo = sqrt(reduce(g, mo))
        self.px /= mo
        self.py /= mo
        self.pz /= mo

class Ray:
    def __init__(self, ori, dir):
        self.direction = dir
        self.origin = ori

class Camera:
    def __init__(self, height, width, eye_pos=Vector3(0, 0, 0)):

        self.eye_position = eye_pos

        # the three basis of the camera
        self.V = Vector3(0, 0, 1)
        self.W = Vector3(0, -1, 0)
        self.U = self.V.X(self.W)

        # the fllowing h and w are the size of the origin image
        self.window_H = height
        self.window_W = width

        # keep the scale of the view plane
        self.plane_H = 1000
        self.plane_W = self.plane_H * width/height

        # top down left right of the view plane
        self.t = self.plane_H / 2
        self.b = -self.plane_H / 2
        self.l = -self.plane_W / 2
        self.r = self.plane_W / 2

        # distance from the eye to the view plane
        self.d = 1000


    def ray_generator(self, i, j):
        u = self.l + self.plane_W * ((j+0.5) / self.window_W)
        v = self.b + self.plane_H * ((i+0.5) / self.window_H)

        # print((j+0.5) / self.window_W)
        # print((i+0.5) / self.window_H)
        # print("in the fun ray_generator",u,v)

        uU = self.U.s_multip(u)
        vV = self.V.s_multip(v)
        _dW = self.W.s_multip(-1 * self.d)

        # -dW + uU +vV
        dir = _dW.plus(vV).plus(uU)
        ori = self.eye_position

        return Ray(ori, dir)

