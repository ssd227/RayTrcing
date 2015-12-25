from vector import *

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
        dir.normalize()

        ori = self.eye_position

        return Ray(ori, dir)

